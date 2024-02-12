# django
from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import TemplateView, ListView

# models
from pages.models import BannerModel
from products.models import ProductModel
from blogs.models import PostModel

# Create your views here.
class HomePageView(ListView):
    template_name = "home.html"
    model = BannerModel
    
    def get_queryset(self):
        return BannerModel.objects.filter(is_active=True)


class ShopPageView(ListView):
    template_name = "shop.html"
    model = ProductModel


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