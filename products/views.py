from typing import Any
from django.db import IntegrityError
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView

from products.models import ProductModel, WishlistModel

# Create your views here.
class WishlistPageView(ListView):
    template_name = 'wishlist.html'
    model = WishlistModel
    context_object_name = "wishlists"

    def get_queryset(self):
        return WishlistModel.objects.filter(user=self.request.user)


@login_required
def add_to_wishlist(request, product_pk):
    product = ProductModel.objects.get(pk=product_pk)
    current_path_url = request.META.get("HTTP_REFERER")

    try:
        WishlistModel.objects.create(user=request.user, product=product)
        return redirect(current_path_url)
    except IntegrityError:
        WishlistModel.objects.get(user=request.user, product=product).delete()
        return redirect(current_path_url)


class ShopDetailView(DetailView):
    template_name = "shop-details.html"
    model = ProductModel
    context_object_name = "product"