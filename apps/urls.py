from django.urls import path
from .views import homepage, add_product, add_user, add_category, generate_data

urlpatterns = [
    path('', homepage, name='homepage'),
    path('add_product', add_product, name='add_product'),
    path('add_user', add_user, name='add_user'),
    path('add_category', add_category, name='add_category'),
    path('data', generate_data, name='generate_data')
]