from django.views import View
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.core.serializers import serialize
from django.contrib.auth.models import User
from django.views.generic.detail import DetailView


from .forms import UserRegistrationForm
from .models import Category, Product


class ProductDetailView(DetailView):
	model = Product

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(**kwargs)
		pass


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
	if request.is_ajax():
		print('это аякс')
	count = 0
	products = Product.objects.filter(category=2)
	count += len(products)
	context = {'products': products}
	return render(request, 'home/candleholder.html', context=context)


class DynamicProductsLoad(View):

	@staticmethod
	def get(request, *args, **kwargs):
		last_product_id = request.GET.get('lastProductId')
		a = Category.objects.filter(name__iexact='Подсвечники').select_related('product')
		more_products = Product.objects.filter(id__gt=last_product_id).values('id', 'title', 'description', 'price')[:2]
		if not more_products:
			return JsonResponse({'data': False})
		data = []
		for product in more_products:
			obj = {
				'id': product['id'],
				'title': product['title'],
				'description': product['description'],
				'price': product['price'],
			}
			data.append(obj)
			data[-1]['last_product'] = True
			return JsonResponse({'data': data})



def show_wrapper(request):
	"""Отображает страницу упаковки"""
	wrappers = Product.objects.filter(category=6)
	context = {'wrappers': wrappers}
	return render(request, 'home/wrapper.html', context=context)


def show_pigment(request):
	"""Отображает страницу красители"""
	pigments = Product.objects.filter(category=4)
	context = {'pigments': pigments}
	return render(request, 'home/pigment.html', context=context)


def show_instrument(request):
	"""Отображает страницу инструмент"""
	instruments = Product.objects.filter(category=3)
	context = {'instruments': instruments}
	return render(request, 'home/instrument.html', context=context)


def show_equipment(request):
	"""Отображает страницу подсвечников, в фильтре категория по id=2(подсвечники) таблицы Category"""
	equipments = Product.objects.filter(category=7)
	context = {'equipments': equipments}
	return render(request, 'home/equipment.html', context=context)


def show_candle_molds(request):
	"""Отображает страницу подсвечников, в фильтре категория по id=2(подсвечники) таблицы Category"""
	silicon_molds = Product.objects.filter(category=5)
	context = {'silicon_molds': silicon_molds}
	return render(request, 'home/candle_molds.html', context=context)


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
	ask = User.objects.filter(username__iexact=username).exists()
	response = {
		'is_taken': ask
	}
	return JsonResponse(response)


def add_product(request):
	if request.method == 'GET':
		data = {
			'text': request.GET['text'],
			'num': request.GET['num'],
		}
		print(data)
