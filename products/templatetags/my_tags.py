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
    if coupon:
        total_price = total_price - ((total_price / 100) * coupon.discount)
    return quantity, "{:.2f}".format(total_price)


@register.filter(name='in_cart')
def in_cart(request, pk):
    cart = request.session.get("cart", [])
    if pk in cart:
        return True
    else:
        return False