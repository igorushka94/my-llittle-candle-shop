from django.forms.forms import Form
from home.models import Product
from django import forms
# from django.contrib.auth.models import User
# from django.db import models
# from django.db.models import fields
# from django.forms.forms import Form
# from django.forms.widgets import Textarea


PRODUCT_QUANTITY_CHOICERS = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    # quantity – количество единиц товара (доступны значения от 1 до 20), coerce=int - преобразовывать выбранное значение в целое число;
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICERS, coerce=int)
    """
    update – обновить (значение True) или заменить (значение False) количество единиц для товара.
    Используется тип поля HiddenInput, чтобы пользователь не видел его в своей форме.
    """
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

# class CandleForm(forms.ModelForm):
#     title = forms.CharField(label='Название товара')
#     content = forms.CharField(widget=Textarea, label='Описание товара')
#     price = forms.FloatField(label='Цена')

#     class Meta:
#         model = Candle
#         fields = ('title', 'content', 'price')


# """class LoginForms(forms.Form):
#     username = forms.CharField()
#     password = forms.CharField(widget=forms.PasswordInput)

# class UserRegistrationForm(forms.ModelForm):
#     password = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)
#     class Meta:
#     model = User
#     fields = ('username', 'first_name', 'email')
#     def clean_password2(self):
#     cd = self.cleaned_data
#     if cd['password'] != cd['password2']:
#     raise forms.ValidationError('Passwords don\'t match.')
#     return cd['password2']"""