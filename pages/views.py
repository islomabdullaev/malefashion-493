# django
from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import TemplateView, ListView

# models
from pages.models import BannerModel
from products.models import BrandModel, CategoryModel, ColorModel, CouponModel, ProductModel, SizeModel, TagModel
from blogs.models import PostModel
from django.db.models import Min, Max

# Create your views here.
class HomePageView(ListView):
    template_name = "home.html"
    model = BannerModel
    
    def get_queryset(self):
        return BannerModel.objects.filter(is_active=True)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = ProductModel.objects.all()
        context["posts"] = PostModel.objects.all().order_by("-created_at")[:3]
        
        return context

class ShopPageView(ListView):
    template_name = "shop.html"
    model = ProductModel
    context_object_name = "products"
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = CategoryModel.objects.all()
        context['brands'] = BrandModel.objects.all()
        context['sizes'] = SizeModel.objects.all()
        context['colors'] = ColorModel.objects.all()
        context['tags'] = TagModel.objects.all()
        context['min_price'] = ProductModel.objects.aggregate(min_price=Min("price"))['min_price']
        context['max_price'] = ProductModel.objects.aggregate(max_price=Max("price"))['max_price']

        return context
    

    def get_queryset(self):
        products = ProductModel.objects.all().order_by('price')
        sort = self.request.GET.get("sort")
        q = self.request.GET.get("q")
        category = self.request.GET.get('category')
        brand = self.request.GET.get('brand')
        size = self.request.GET.get('size')
        color = self.request.GET.get('color')
        tag = self.request.GET.get('tag')
        from_price = ProductModel.objects.aggregate(min_price=Min("price"))['min_price']
        to_price = ProductModel.objects.aggregate(max_price=Max("price"))['max_price']
        price_range = self.request.GET.get("my_range")
        if price_range:
            self.paginate_by = len(ProductModel.objects.all())
            price_range = self.request.GET.get("my_range").split(";")
            from_price, to_price = price_range[0], price_range[1]
        if sort:
           products = products.order_by(sort)
        elif q:
            products = products.filter(name__icontains=q)
        elif category:
            products = products.filter(category__title=category)
        elif brand:
            products = products.filter(brand__title=brand)
        elif size:
            products = products.filter(sizes__title=size)
        elif color:
            products = products.filter(colors__name=color)
        elif tag:
            products = products.filter(tags__title=tag)
        elif from_price and to_price:
            products = products.filter(price__range=(float(from_price), float(to_price)))

        return products



class AboutPageView(TemplateView):
    template_name = "about.html"


class BlogPageView(ListView):
    template_name = "blog.html"
    model = PostModel
    context_object_name = "posts"

    def get_queryset(self):
        tag = self.request.GET.get("tag")
        posts = PostModel.objects.all()
        if tag:
            posts = PostModel.objects.filter(tags__title=tag)
        return posts


class ContactsPageView(TemplateView):
    template_name = "contact.html"


class CartListView(ListView):
    template_name = "shopping-cart.html"
    model = ProductModel
    context_object_name = "products"

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        code = self.request.GET.get("coupon")
        if code:
            try:
                coupon = CouponModel.objects.filter(code=code, is_active=True)
                context['coupon'] = coupon
            except CouponModel.DoesNotExist:
                context['coupon'] = None
        return context

    def get_queryset(self):
        cart = self.request.session.get("cart", [])
        products = ProductModel.objects.filter(pk__in=cart)

        return products