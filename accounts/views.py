import re
from django import forms
from django.shortcuts import redirect, render
from django.contrib.auth.views import LogoutView
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from home.models import Customer
from .forms import ImgForm


class MyLogoutView(LogoutView):
    next_page = None
    template_name = 'accounts/logged_out.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def get_to_user_profile(request):
    username = request.user
    user = User.objects.get(username__exact=username)
    customer = user.customer_set.get(user=username)
    context = {
        'fname': user.first_name,
        'lname': user.last_name,
        'email': user.email,
        'phone': customer.phone,
        'address': customer.address,
        'photo': customer.image
    }
    return render(request, template_name='accounts/profile.html', context=context)


def delete_user_data(request):
    pass


def update_user_data(request): 
    pass


def add_user_photo(request):
    if request.method == "POST":
        form = ImgForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('accounts:get_to_user_profile')
        else:
            form = ImgForm()
            context = {'form': form}
            return render(request, 'accounts/profile.html', context)


@csrf_exempt
def delete_photo_in_account(request):
    """Удаляет фото профиля на странице в accounsts/profile"""
    username = request.user
    customer = Customer.objects.get(user=username)
    if request.method == 'GET':
       customer.image = ''
       customer.save()
    return render(request, 'accounts/profile.html')