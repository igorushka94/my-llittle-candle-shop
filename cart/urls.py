from os import name
from django.urls import path

from . import views


app_name = 'cart'
urlpatterns = [
    path('', views.show_cart, name='show_cart'),
    path('add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    #path('', views.create_order, name='create_order')
]