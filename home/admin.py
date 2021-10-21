from django.contrib import admin
from .models import Category, Product, CardProduct, Customer, Order, OrderProduct


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slag')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'category', 'title', 'description', 'price')


class CardProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', )


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'phone', 'address')


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'date_create', 'date_update')


class OrderProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'count', 'final_price')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(CardProduct, CardProductAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProduct, OrderProductAdmin)
