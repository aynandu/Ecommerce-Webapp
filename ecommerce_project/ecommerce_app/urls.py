
from django.urls import path

from ecommerce_app import views
app_name='ecommerce_app'

urlpatterns = [
    path('',views.allProductCat,name='allProductCat'),
    path('<slug:c_slug>/',views.allProductCat,name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/',views.proDetails,name="proCatDetails"),
]