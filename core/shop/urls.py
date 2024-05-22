from django.urls import path
from .views import *

urlpatterns = [
    path('', main_view, name='start_page'),
    path('categries/', category_list_view, name='categories'),
]
