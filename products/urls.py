from django.urls import path

from products.views import ShopDetailView, WishlistPageView, add_to_wishlist, add_to_cart, add_cart_data

app_name = 'products'

urlpatterns = [
    path('<int:pk>/details/', ShopDetailView.as_view(), name="details"),
    path('wishlist/', WishlistPageView.as_view(), name='wishlist'),
    path('<int:product_pk>/add_to_wishlist/', add_to_wishlist, name='add_to_wishlist'),
    path('<int:pk>/add_to_cart/', add_to_cart, name='add_to_cart'),
    path('<int:pk>/quantity/<int:quantity>/', add_cart_data, name='add_cart_data')
]