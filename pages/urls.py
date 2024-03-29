# urls
from django.urls import path

# views
from pages.views import (
    CartListView, HomePageView, ShopPageView, AboutPageView,
    BlogPageView, ContactsPageView)

app_name = 'pages'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('shop/', ShopPageView.as_view(), name='shop'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('blog/', BlogPageView.as_view(), name='blog'),
    path('contact/', ContactsPageView.as_view(), name='contact'),
    path('cart/', CartListView.as_view(), name='cart')
]