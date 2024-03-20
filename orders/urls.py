from django.urls import path
from orders.views import proceed_order

app_name = "orders"

urlpatterns = [
    path('proceed_order/', proceed_order, name="proceed_order")
]