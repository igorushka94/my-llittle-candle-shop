from django.urls import path
from . import views


app_name = 'home'
urlpatterns = [
    path('register/', views.register, name='register'),
    path('test_form/', views.delivery, name='delivery'),
    path('validate_username/', views.validate_username, name='validate_username'),
    path('wrapper/', views.show_wrapper, name='wrapper'),
    path('pigment/', views.show_pigment, name='pigment'),
    path('instrument/', views.show_instrument, name='instrument'),
    path('equipment/', views.show_equipment, name='equipment'),
    path('candle_molds/', views.show_candle_molds, name='candle_molds'),
    path('candle/add_product/', views.add_product, name='add_product'),
    path('candle/', views.show_candle, name='candle'),
    path('candleholder/', views.show_candleholder, name='candleholder'),
    path('load-more-products/', views.DynamicProductsLoad.as_view(), name='load-more-products'),
    path('delivery/', views.delivery, name='delivery'),
    path('test/', views.test, name='test'),
    path('test2/', views.test2, name='test2'),
    path('', views.BaseView.as_view(), name='index'),
]
