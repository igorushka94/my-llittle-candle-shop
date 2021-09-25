# from django.contrib import admin


# from .models import Candle, Cart, Delivery, Product, SiliconMold


# class ProductAdmin(admin.ModelAdmin):
# 	list_display = ('title',)
# 	list_display_link = ('title',)
# 	search_fields = ('title',)


# class CandleAdmin(admin.ModelAdmin):
# 	list_display = ('product','title', 'content', 'price', 'published', 'image') #последовательность имён полей, которые должны выводиться в списке записей
# 	list_display_link = ('title', 'content') #последовательность имён полей, которые должны быть преобразованы в гиперссылки, ведущие на страницу правки записи
# 	search_fields = ('title', 'content') #последовательность имён полей, по которым должна выполняться фильтрация


# class SiliconMoldAdmin(admin.ModelAdmin):
# 	list_display = ('product', 'title', 'content', 'price', 'image')
# 	list_display_link = ('title', 'content', 'price', 'image')
# 	search_fields = ('title', 'content', 'price', 'image')


# class CartAdmin(admin.ModelAdmin):
# 	list_display = ('title', 'content', 'price_per_unit', 'count', 'total_amount')
# 	list_display_link = ('title', 'content')
# 	search_fields = ('title', 'content', 'price_per_unit', 'count', 'total_amount')


# class DeliveryAdmin(admin.ModelAdmin):
# 	list_display = ('first_name', 'phone', 'addr_delivery', 'pay_method', 'comment_order')
# 	list_display_link = ('first_name', 'phone')
# 	search_fields = ('first_name', 'phone', 'addr_delivery')


# admin.site.register(Product, ProductAdmin)
# admin.site.register(SiliconMold, SiliconMoldAdmin)
# admin.site.register(Candle, CandleAdmin)
# admin.site.register(Cart, CartAdmin)
# admin.site.register(Delivery, DeliveryAdmin)


from django.contrib import admin
from .models import Category, Product, Cart, CardProduct, Order, CartProduct, Customer, Client


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slag')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('category', 'title', 'description', 'price')


class CardProductAdmin(admin.ModelAdmin):
    list_display = ('product', )


class OrderAdmin(admin.ModelAdmin):
    list_display = ('card_product', 'date')


class CartAdmin(admin.ModelAdmin):
    list_display = ('owner', 'total_products', 'final_price')


class CartProductAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'qty', 'final_price')


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'address')


class ClientAdmin(admin.ModelAdmin):
    list_display = ('ip', 'refer', 'user_agent', 'date')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(CardProduct, CardProductAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(CartProduct, CartProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Client, ClientAdmin)
