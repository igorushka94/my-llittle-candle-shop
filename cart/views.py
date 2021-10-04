import cart
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST, require_http_methods

from home.models import Product
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                quantity=cd['quantity'],
                update_quantity=cd['update'])
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    """Отображает корзину основываясь на данных сессии, сохранённых в request.session"""
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})

def show_cart(request):
    return render(request, 'cart/detail.html')

# class CartTemplateView(TemplateView):
#     model = Cart
#     template_name = 'cart/cart.html'
#     #form_class = CandleForm


#     def count_product():
#         """Количество товаров в корзине"""
#         return count

#     def price_product():
#         """Стоимость товаров в корзине"""
        
        
#     def price_delivery():
#         """Стоимость доставки"""
#         pass

#     def total_price():
#         """Общая стоимость товара в корзине"""
#         pass



# """def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request, username=cd['username'], password=cd['password'])

#         if user is not None:
#             if user.is_active:
#                 login(request, user)
#                 return HttpResponse('Authenticated successfully')
#             else:
#                 return HttpResponse('Disabled account')
#         else:
#             return HttpResponse('Invalid login')
#     else:
#         form = LoginForm()
#         return render(request, 'account/login.html', {'form': form})"""