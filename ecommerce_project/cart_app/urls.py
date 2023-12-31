from django.urls import path 
from . import views

app_name='cart_app'

urlpatterns=[
    path('add/<int:product_id>/',views.add_cart,name ='add_cart'),
    path('',views.cart_details,name='cart_detail'),
    path('remove/<int:product_id>/',views.cart_remove,name='remove_cart'),
    path('delete/<int:product_id>',views.cart_delete,name='delete_cart'),
]