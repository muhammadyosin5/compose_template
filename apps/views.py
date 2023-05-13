from django.shortcuts import render, redirect
from .models import Product, Category
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from faker import Faker
from django.views.decorators.csrf import csrf_exempt


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'password1', 'password2')


@csrf_exempt
def homepage(request):
    return render(request, 'apps/index.html')


@csrf_exempt
def add_product(request):
    if request.method == 'POST':
        Product.objects.create(name=request.POST.get('name'), price=request.POST.get('price'))
        print('Product Saved!')
    return redirect('homepage')

@csrf_exempt
def add_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    return redirect('homepage')


def add_category(request):
    if request.method == 'POST':
        Category.objects.create(name=request.POST.get('name'))
        print('Category Saved!')
    return redirect('homepage')


def generate_data(request):
    fake = Faker()
    objects = (Category(name=fake.name()) for _ in range(100_000))
    Category.objects.bulk_create(objects)
    return redirect('homepage')