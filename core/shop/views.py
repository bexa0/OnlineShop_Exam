from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import DetailView
import datetime
from django.core.paginator import Paginator

from .models import *


def main_view(request):
    # pic = Product.objects.all()
    # all_photos = []
    #
    # for p in pic:
    #     photo = Product.objects.filter(image=p)
    #     all_photos.extend(photo)
    #  'all_photos': all_photos
    context = {'categories': Category.objects.all(), 'products': Product.objects.all()}

    return render(request, 'shop/main.html', context)


def category_list_view(request):
    p = Paginator(Category.objects.all(), 4)
    context = {'cat': Category.objects.all()}

    return render(request, 'shop/categories.html', context)


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'shop/category_detail.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        products = Product.objects.filter(category=self.object)
        context['products'] = products
        return context


def cart(request):
    my_cart = request.session.get('cart', [])
    if request.method == 'POST':
        cart_item = request.POST.get('cart_item')
        if request.POST.get('add'):
            for i in my_cart:
                if i['product'] == int(cart_item):
                    i['quantity'] += 1
                    break
        elif request.POST.get('remove'):
            for i in my_cart:
                if i['product'] == int(cart_item):
                    i['quantity'] -= 1
                    if i['quantity'] == 0:
                        my_cart.remove(i)
                    break
            # messages.add_message(request, messages.INFO, f'Removed successfully')
        request.session.modified = True
        return redirect('cart')  # Решается проблема повторной отправки формы
    my_cart_context = []
    total_price = 0
    for item in my_cart:
        my_cart_item = {}
        my_cart_item['product'] = Product.objects.get(pk=item['product'])
        my_cart_item['quantity'] = item['quantity']
        my_cart_item['total'] = float(my_cart_item['product'].price * my_cart_item['quantity'])
        my_cart_context.append(my_cart_item)
        item_price = my_cart_item['product'].price * item['quantity']
        total_price += item_price
        my_cart_context.append(my_cart_item)
    processed_cart = Cart.objects.filter(user=request.user)[3::-1]

    context = {'cart_items': my_cart_context, 'total_price': total_price, 'processed_cart': processed_cart}
    return render(request, 'shop/cart.html', context)


def add_to_cart(request, product_id):
    if not request.session.get('cart'):
        request.session['cart'] = []
    cart = request.session['cart']
    items = [i['product'] for i in cart]
    if product_id in items:
        for i in cart:
            if i['product'] == product_id:
                i['quantity'] += 1
                break
    else:
        cart_item = {
            "product": product_id,
            "quantity": 1
        }
        cart.append(cart_item)

    request.session.modified = True
    product = Product.objects.get(pk=product_id)
    category_id = product.category.pk
    # messages.add_message(request, messages.INFO, f"Product {product.name} added successfully")

    return redirect('category_detail', category_id)


def favorite(request):
    my_favorite = request.session.get('favorite', [])
    if request.method == 'POST':
        if request.POST.get('add'):
            print(my_favorite)

    return render(request, 'shop/favorites.html')


def add_to_favorite(request, id):
    if request.method == 'POST':
        if not request.session.get('favorites'):
            request.session['favorites'] = list() # если нету то создает пустой список
        else:
            request.session['favorites'] = list(request.session['favorites']) # если есть то создает список с предудушими значениями которые были записаны

        item_exist = next((item for item in request.session['favorites'] if item['type'] == request.POST.get('type') and item['id'] == id), False)

        add_data = {
            'type': request.POST.get('type'),
            'id': id,
        }

        if not item_exist:
            request.session['favorites'].append(add_data)
            request.session.modified = True
    return redirect(request.POST.get('favorite'))


def contact(request):
    contact_inf = Contact.objects.all()
    context = {'contacts': contact_inf}

    return render(request, 'shop/contact.html', context)


def about(request):
    return render(request, 'shop/about.html')


# def latest_objects(request):
#     products = Product.objects.all().order_by('-created')[0]
#     context = {'latest_pr': products}
#
#     return render(request, 'shop/latest_products.html', context)
