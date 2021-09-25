# from django.db import models
# from django.contrib.auth import get_user_model
# from django.db.models.deletion import CASCADE, PROTECT
# from django.db.models.fields import EmailField


# User = get_user_model()

#********************
#1 Category ---
#2 Product ---
#3 CartProduct ---
#4 Cart
#5 Order
#********************
#6 Castomer
#7 Specification 

"""class Order(models.Model):
    """  """
    fname = models.CharField(verbose_name='Имя')
    lname = models.CharField(verbose_name='Фамилия')
    phone_number = models.DecimalField(max_digits=11, decimal_places=0, verbose_name='Номер телефона', help_text='<p>Введите Ваш номер телефона</p>')
    email_addr = models.EmailField(verbose_name='email')
    comment = models.CharField(verbose_name='Комментарий к заказу', max_length=255)

    def __str__(self) -> str:
        return "Заказ"


class Сustomer(models.Model):
    """  """
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=CASCADE)
    phone = models.CharField(max_length=20, verbose_name='Номер телефона')
    address = models.CharField(max_length=255, verbose_name='Адресс')

    def __str__(self) -> str:
        return "Покупатель: {} {}".format(self.user.first_name, self.user.last_name)


class Cart(models.Model):
    """  """
    owner = models.ForeignKey('Customer', verbose_name='Владелец', on_delete=CASCADE)
    candle = models.ForeignKey('home.Candle', on_delete=PROTECT)
    total_products = models.PositiveIntegerField(default=0)
    total_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Общая цена')

    def __str__(self) -> str:
        return str(self.id)

"""