from django.shortcuts import get_object_or_404, render,redirect
from ecommerce_app.models import Product
from . models import Cart,CartItem
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

#Create a Cart id for a session
def _cart_Id(request):
    cart=request.session.session_key
    if not cart :
        cart=request.session.create()
    return cart

def add_cart(request,product_id):
    product=Product.objects.get(id=product_id)
    try:
        cart=Cart.objects.get(cart_id=_cart_Id(request))
    except Cart.DoesNotExist:
        cart=Cart.objects.create(cart_id=_cart_Id(request))
        cart.save()
    try:
        cart_item=CartItem.objects.get(product=product,cart=cart)
        if cart_item.quantity < cart_item.product.stock:
            cart_item.quantity+=1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item=CartItem.objects.create(
            product=product,cart=cart,quantity=1
        )
        cart_item.save()
    return redirect('cart_app:cart_detail')    

def cart_details(request,total=0,counter=0,cart_items=None):
    try:
        cart=Cart.objects.get(cart_id=_cart_Id(request))
        cart_items=CartItem.objects.filter(cart=cart,active=True)
        for cart_item in cart_items:
            total+=(cart_item.product.price * cart_item.quantity)
            counter+=cart_item.quantity
    except ObjectDoesNotExist:
        pass
    return render(request,'cart.html',dict(total=total,cart_items=cart_items,counter=counter))

def cart_remove(request,product_id):
    cart=Cart.objects.get(cart_id=_cart_Id(request))
    product=get_object_or_404(Product,id=product_id)
    cart_items=CartItem.objects.get(product=product,cart=cart)
    if cart_items.quantity > 1:
        cart_items.quantity -= 1
        cart_items.save()
    else:
        cart_items.delete()
    return redirect('cart_app:cart_detail')

def cart_delete(request,product_id):
    cart=Cart.objects.get(cart_id=_cart_Id(request))
    product=get_object_or_404(Product,id=product_id)
    cart_items=CartItem.objects.get(product=product,cart=cart)
    cart_items.delete()
    return redirect('cart_app:cart_detail')