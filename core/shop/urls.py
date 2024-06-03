from django.urls import path
from .views import *

urlpatterns = [
    path('', main_view, name='start_page'),
    path('category/', category_list_view, name='categories'),
    path('category/detail/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('cart/', cart, name='cart'),
    path('add-card/<int:product_id>/', add_to_cart, name='add_to_cart'),
    # path('new-arrivals/', latest_objects, name='latest_obj'),
    path('favorites/', favorite, name='favorites'),
    path('contacts/', contact, name='contact'),
    path('about/', about, name='about'),
]
