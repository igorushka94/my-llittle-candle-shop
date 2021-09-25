from django.urls import path
from . import views


app_name = 'home'
urlpatterns = [
    path('register/', views.register, name='register'),
#     path('add_to_cart/', add_to_cart, name='add'),
#     path('test_form/', delivery, name='delivery'),
#     path('product/candles/', show_candles, name='candles'),
#     path('product/silicon_mold/', show_silicon_mold, name='silicon_mold'),
    path('validate_username/', views.validate_username, name='validate_username'),
    path('wrapper/', views.show_wrapper, name='wrapper'),
    path('pigment/', views.show_pigment, name='pigment'),
    path('instrumenst/', views.show_instrumenst, name='instrumenst'),
    path('equipment/', views.show_equipment, name='equipment'),
    path('candle_molds/', views.show_candle_molds, name='candle_molds'),
    path('candle/', views.show_candle, name='candle'),
    path('candleholder/', views.show_candleholder, name='candleholder'),
    path('delivery/', views.delivery, name='delivery'),
    path('test/', views.test, name='test'),
    path('test2/', views.test2, name='test2'),
    path('', views.BaseView.as_view(), name='index'),
]
