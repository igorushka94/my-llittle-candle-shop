from decimal import Decimal

from django.contrib.auth import get_user_model
from django.db import models

from .logic import get_timestamp_path


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


class Category(models.Model):
    """
    Категория
    """
    name = models.CharField(max_length=255, verbose_name='Имя категории')
    slag = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    @staticmethod
    def count_product_in_categories():
        """
        Подсчёт количества(позиций) товаров в каждой категории
        """
        from django.db.models import Count

        counts = Category.objects.annotate(Count('product'))
        return counts


class Product(models.Model):
    """
    Таблица Продукт, отношение 1 ко многим от Product к набору Category
    """
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name='Категория'
        )

    title = models.CharField(max_length=255, verbose_name='Наименование')
    description = models.CharField(max_length=255, blank=True, verbose_name='Описание')
    available = models.BooleanField(default=True, verbose_name='В наличии')
    image = models.ImageField(blank=True, upload_to=get_timestamp_path, verbose_name='Изображение')
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['title', 'price']

    def __str__(self):
        return self.title


class CardProduct(models.Model):
    """
    Карточка продукта
    """
    product = models.ForeignKey(Product, verbose_name='Карточка продукта', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Карта продукта'
        verbose_name_plural = 'Карты продукта'


class Order(models.Model):
    """
    Заказ
    """
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, verbose_name='Логин')
    order_product = models.ManyToManyField(
        Product,
        through='OrderProduct',
        through_fields=('order', 'product')
    )
    date_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заказа')
    date_update = models.DateTimeField(auto_now=True, verbose_name='Дата оформления заказа')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ['-date_create']
        get_latest_by = ['-date_create']

    def __str__(self):
        return f'Заказ № {self.id}, пользователя {self.customer.user.username}'


class OrderProduct(models.Model):
    """
    ЗаказПродукт 
    """
    order = models.OneToOneField(
        Order,
        on_delete=models.CASCADE,
        verbose_name='Заказ',
        )

    product = models.OneToOneField(
        Product,
        on_delete=models.CASCADE,
        verbose_name='Товар', 
       )

    count = models.PositiveIntegerField(default=1, verbose_name='Количество товара')
    final_price = models.DecimalField(max_digits=9, decimal_places=2, blank=True, verbose_name='Общая цена')

    class Meta:
        verbose_name = 'Заказ продукт'
        verbose_name_plural = 'Заказы продукты'

    def calculate_final_price(self):
        self.final_price = self.product.price * self.count
        return self.final_price

    def save(self, *args, **kwargs):
        self.final_price = self.calculate_final_price()
        super().save(*args, **kwargs)


class Customer(models.Model):
    """
    Модель Покупатель
    """
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE,
        verbose_name='Покупатель', 
        )

    phone = models.CharField(max_length=20, verbose_name='Нормер телефона')
    address = models.CharField(max_length=255, verbose_name='Адрес')
    image = models.ImageField(blank=True, upload_to=get_timestamp_path, verbose_name='Изображение')

    class Meta:
        verbose_name = 'Покупатель'
        verbose_name_plural = 'Покупатель'

    def __str__(self):
        return self.user.username
