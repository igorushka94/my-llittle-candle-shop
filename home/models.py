from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()

# ********Таблицы*********
# Категория
# Продукт
# Карточка продукта
# Заказ
# Продукт в корзине
# Корзина
# Покупатель
# ********Конец***********

def get_timestamp_path(isinstance, filename):
    from datetime import datetime
    from os.path import splitext

    return '%s%s' % (datetime.now().timestamp(), splitext(filename)[1])

class Category(models.Model):
    """Категория"""
    name = models.CharField(max_length=255, verbose_name='Имя категории')
    slag = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    @staticmethod
    def count_product_in_categories():
        """Подсчёт количества(позиций) товаров в каждой категории"""
        from django.db.models import Count

        counts = Category.objects.annotate(Count('product'))
        return counts


class Product(models.Model):
    """Продукт"""
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.CASCADE)

    title = models.CharField(max_length=255, verbose_name='Наименование')
    description = models.CharField(max_length=255, blank=True, verbose_name='Описание')
    available = models.BooleanField(default=True, verbose_name='В наличии')
    image = models.ImageField(blank=True, verbose_name='Изображение')
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['title', 'price']

    def __str__(self):
        return self.title


class CardProduct(models.Model):
    """Карточка продукта"""
    product = models.ForeignKey(Product, verbose_name='Карточка продукта', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Карта продукта'
        verbose_name_plural = 'Карты продукта'


class Order(models.Model):
    """Заказ"""
    card_product = models.OneToOneField('Cart', verbose_name='ID корзины', on_delete=models.CASCADE)

    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата заказа')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['-date']
        get_latest_by = '-date'


class CartProduct(models.Model):
    """Продукт в корзине""" 
    user = models.ForeignKey('Customer', verbose_name='Покупатель', on_delete=models.CASCADE)
    cart = models.ForeignKey('Cart', verbose_name='Корзина', on_delete=models.CASCADE, related_name='related_products')
    product = models.ForeignKey(Product, verbose_name='Продукт', on_delete=models.CASCADE)

    qty = models.PositiveIntegerField(default=1, verbose_name='Количество товара')
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Общая цена')

    class Meta:
        verbose_name = 'Продукт в корзине'
        verbose_name_plural = 'Продукты в корзине'

    def __str__(self):
        return f"Продукт {self.product.title}"

    def calculate_final_price(self):
        final_price = self.qty * self.product.price
        return final_price


class Cart(models.Model):
    """Корзина"""
    owner = models.ForeignKey('Customer', verbose_name='Владелец', on_delete=models.CASCADE)
    products = models.ManyToManyField(CartProduct, blank=True, verbose_name='Товары в корзине', related_name='related_cart')

    total_products = models.PositiveIntegerField(default=0, verbose_name='Общее количество товаров')
    final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Общая цена')

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return str(self.id)


class Customer(models.Model):
    """Покупатель"""
    user = models.ForeignKey(User, verbose_name='Покупатель', on_delete=models.CASCADE)

    phone = models.CharField(max_length=20, verbose_name='Нормер телефона')
    address = models.CharField(max_length=255, verbose_name='Адрес')
    image = models.ImageField(blank=True, upload_to=get_timestamp_path, verbose_name='Изображение')

    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатель'

    def __str__(self):
        return self.user.username

    def check_photo_profile(self) -> bool:
        """Проверят наличие фото в базе, возвращает True или False"""
        if self.image == None:
            return False


class Client(models.Model):
    ip = models.GenericIPAddressField(verbose_name='IP-адрес')
    refer = models.TextField(verbose_name='Рефер')
    user_agent = models.TextField(verbose_name='User-агент')
    date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
