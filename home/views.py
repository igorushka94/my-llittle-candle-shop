from django.views import View
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.core.serializers import serialize
from django.contrib.auth.models import User


from .forms import UserRegistrationForm
from .models import Category, Product


def prodcut_list(request):
	category = None
	categories = Category.objects.all()
	products = Product.objects.filter(availabel=True)
	if category_slug: 
		category = get_object_or_404(Category, slug=category_slug)
		products = products.filter(category=category)
	return render(
		request, 
		'home/product/list.html', 
		{'category': category,
		'categories':categories,
		'products':products,})


def product_detail(request, id, slug):
	product = get_object_or_404(Product, id=id, slug=slug, available=True)
	return render(request, 'home/product/detail.html', {'product': product})
	

def test(request):	
	products =  Product.objects.all()[0:1]
	json = serialize("json", products)
	return JsonResponse(data=json, json_dumps_params={}, safe=False)


def test2(request):
	if request.is_ajax():
		data = serialize('json', Product.objects.all()[:2])
		return JsonResponse(data=data, safe=False,)


def delivery(request):
	return render(request, template_name='home/delivery.html')

class BaseView(View):

	def get(self, request, *args, **kwargs):
		categories = Category.count_product_in_categories()
		context = {'categories': categories, }
		return render(request, 'layout/basic.html', context=context)


def show_candle(request):
	products = Product.objects.filter(category=1)
	paginator = Paginator(products, 8)
	if 'page' in request.GET:
		page_num = request.GET['page']
	else:
		page_num = 1
	page = paginator.get_page(page_num)
	context = {'products': page.object_list, 'page': page,}
	return render(request, 'home/candles.html', context=context)


def show_candleholder(request):
	"""Отображает страницу подсвечников, в фильтре категория по id=2(подсвечники) таблицы Category"""
	products = Product.objects.filter(category=2)
	context = {'products': products}
	return render(request, 'home/candleholder.html', context=context)


def show_wrapper(request):
	"""Отображает страницу упаковки"""
	pass


def show_pigment(request):
	"""Отображает страницу красители"""
	pass


def show_instrumenst(request):
	"""Отображает страницу инструмент"""
	pass


def show_equipment(request):
	"""Отображает страницу подсвечников, в фильтре категория по id=2(подсвечники) таблицы Category"""
	pass


def show_candle_molds(request):
	"""Отображает страницу подсвечников, в фильтре категория по id=2(подсвечники) таблицы Category"""
	pass


def register(request):
	""" Обработчик регистрации нового пользователя """
	#Доработать функционал проверки в БД User недопустимость одинаковых email адресов
	if request.method == 'POST':
		user_form = UserRegistrationForm(request.POST)
		if user_form.is_valid():
			new_user = user_form.save(commit=False) # Создаем нового пользователя, но пока не сохраняем в базу данных.
			new_user.set_password(user_form.cleaned_data['password']) # Метод set_password() шифрует пароль.
			new_user.save() # Сохранить пользователя в базе данных.
			return render(request, 'registration/register_done.html', {'new_user': new_user})
	else:
 		user_form = UserRegistrationForm()
	return render(request,'registration/register.html', {'user_form': user_form})


def validate_username(request):
	"""Проверка доступности логина"""
	username = request.GET.get('username', None)
	response = {
		'is_taken': User.objects.filter(username__iexact=username).exists()
	}
	return JsonResponse(response)

