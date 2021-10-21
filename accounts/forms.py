from django import forms
from django.contrib.auth.models import User
from django.core import validators
from home.models import Customer
from django.contrib.auth.forms import AuthenticationForm


class UserModifyForm(forms.ModelForm):
    fname = forms.CharField(
        label='Имя', 
        help_text='Введите имя'
        )
    lname = forms.CharField(
        label='Фамилия', 
        help_text='Введите фамилию'
        )
    email = forms.EmailField(
        label='Новый Email',
        help_text='Введите новый email'
        )
    

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ImgForm(forms.ModelForm):
    img = forms.ImageField(
        label='Изображение',
        validators=[validators.FileExtensionValidator(allowed_extensions=('jpg', 'png'))],
        error_messages={'invalid_extension': 'Этот формат файлов не поддерживается'}
        )
    
    class Meta:
        model = Customer
        fields = ('image',)