from decimal import Decimal
from django import conf
from django.conf import settings

from home.models import Product


class Cart(object):

    def __init__(self, request):
        """Инициализация объекта корзины"""
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # Сохранить в сесии пустую строку
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add(self, product, quantity=1, update_quantity=False):
        """
        Добавление товара в корзину или обновление его количества, принимает 3 параметра
        product – объект модели Product, который нужно добавить или обновить;
        quantity – не являющееся обязательным количество объектов, по умолчанию 1;
        update_quantity – булево значение, которое говорит о том, нужно ли заменить значение 
        количества товаров на новое (True) или следует добавить его к существующему (False)
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart['product_id'] = {'quantity': 0, 'price': str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()


    def save(self):
        # Пометить сессию как измененную
        self.session.modified = True


    def remote(self):
        """Удаление товара из корзины, и сохранение новых данных сессии"""
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart['product_id']
            self.save()


    def __iter__(self):
        """Проходим по товарам корзины и получаем соответствующие объекты Product"""
        product_ids = self.cart.keys()
        # Получаем объекты модели Product и передаем их в корзину
        products = Product.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product
        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
        yield item

    
    def __len__(self):
        """Возвращет общее количество товаров в корзине"""
        return sum(item['quantity'] for item in self.cart.values())


    def get_total_price(self):
        """Подсчёт общей стоимости товаров в корзине"""
        return sum(
            Decimal(item['price'])*item['quantity']
            for item in self.cart.values()
        )


    def clear(self):
        """Очищает корзину"""
        del self.session[settings.CART_SESSION_ID]
        self.save()
