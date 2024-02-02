from django import template
from django.contrib.auth.models import User

from products.models import ProductModel, WishlistModel

register = template.Library()

@register.filter(name="in_wishlist")
def in_wishlist(user, product):
    return WishlistModel.objects.filter(user=user, product=product).exists()