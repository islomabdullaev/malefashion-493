from django import template
from django.contrib.auth.models import User
from django.db.models import Sum

from products.models import ProductModel, WishlistModel

register = template.Library()

@register.filter(name="in_wishlist")
def in_wishlist(user, product):
    return WishlistModel.objects.filter(user=user, product=product).exists()


@register.simple_tag
def get_cart_info(request, coupon=None):
    cart = request.session.get("cart", [])
    products = ProductModel.objects.filter(pk__in=cart)
    total_price = 0
    quantity = len(cart)
    for product in products:
        total_price += float(product.get_real_price())

    return quantity, total_price