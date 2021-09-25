from django import forms
from django.contrib.auth.models import User
from .models import CartProduct


class UserRegistrationForm(forms.ModelForm):
	""" Модельная форма для пользователей, включены только поля username, first_name и email.
		Они будут валидироваться в соответствии с типом полей модели.
		Добавлены 2 поля, password и password2, для задания и подтверждения пароля."""
	password = forms.CharField(label='Пароль', widget=forms.PasswordInput)
	# label - задаёт надписи для полей формы. Словарь 
	# widget - позволяет задать элемент управления, которым будет представляться на вэб-странице поле модели
	password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ('username', 'first_name', 'email')

	def clean_password2(self):
		"""Метод для проверки совпадения паролей password и password2"""
		cd = self.cleaned_data
		if cd['password'] != cd['password2']:
			# Если пароли отличаются то будет возвращена ошибка
			raise forms.ValidationError('Пароли не совпадают')
		return cd['password2']
	

class CartProductForm(forms.ModelForm):
	pass






# class CandleForm(forms.ModelForm):
#     title = forms.CharField(label='Название товара', )
#     content = forms.CharField(widget=Textarea, label='Описание товара')
#     price = forms.FloatField(label='Цена')

#     class Meta:
#         model = Candle
#         fields = ('title', 'content', 'price')


# class CartForm(forms.ModelForm):
#     title = forms.CharField(label='Название товара')
#     content = forms.CharField(widget=Textarea, label='Описание товара')
#     price_per_unit = forms.FloatField(label='Цена')
#     count = forms.DecimalField(max_digits=9, decimal_places=2, label='Количество товара')
#     total_amount = forms.DecimalField(max_digits=9, decimal_places=2, label='Общая сумма')
	
	
#     class Meta:
#         model = Cart
#         fields = ('title', 'content', 'price_per_unit', 'count', 'total_amount')


# class DeliveryForm(forms.ModelForm):
# 	''' Форма доставки товара '''
# 	PAYMENT_METHOD = (
# 		(None, 'Выберете способ оплаты...'),
# 		('a', 'Наличными курьеру'),
# 		('b', 'Оплата картой'),
# 	)
# 	first_name = forms.CharField(max_length=250, label='Ваше имя*', required=True)
# 	# \d{10} - любая цифра ровно 11 раз
# 	phone = forms.RegexField(regex='\+\d{11}', max_length=12, label='Телефон*', initial='+7', required=True)
# 	addr_delivery = forms.CharField(max_length=250, label='Адресс доставки', required=True)
# 	pay_method = forms.ChoiceField(choices=PAYMENT_METHOD, label='Способ оплаты', required=True)
# 	comment_order = forms.CharField(max_length=250, label='Комментарий к заказу', required=False)
		
# 	class Meta:
# 		model = Delivery
# 		fields = ('first_name', 'phone', 'addr_delivery', 'pay_method', 'comment_order')
# 		#labels = 