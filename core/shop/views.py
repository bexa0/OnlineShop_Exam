from django.shortcuts import render
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
    context = {'cat': Category.objects.all()}

    return render(request, 'shop/categories.html', context)
