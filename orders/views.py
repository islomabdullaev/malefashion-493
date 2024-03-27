from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from orders.models import OrderModel, OrderItemModel
from products.models import CouponModel, ProductModel

# Create your views here.


def proceed_order(request):
    cart = request.session.get("cart", [])
    if not cart:
        return HttpResponse("Cart is Empty !")
    products = ProductModel.get_from_cart(cart=cart)
    total_price = 0
    order = OrderModel.objects.create(user=request.user, total_price=0.0)
    for product in products:
        total_price += float(product.get_real_price())
        OrderItemModel.objects.create(product=product, quantity=1, order=order)
    if request.GET.get("total_price"):
        total_price = float(request.GET.get("total_price"))
    code = request.GET.get("code")
    if code:
        updated_coupon = CouponModel.objects.get(code=code)
        updated_coupon.is_active = False
        updated_coupon.save()   
    order.total_price =  float("{:.2f}".format(total_price))
    order.save()
    request.session['cart'] = []
    messages.add_message(request, messages.SUCCESS, "Order Has Been Placed !")
    return redirect("pages:cart")
