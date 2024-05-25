from sqlite3 import IntegrityError
from django.shortcuts import render, redirect
from django.http import HttpResponse
import requests
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import LoginPageSettings, bookstore
from math import ceil

# Create your views here.

def loginn(request):
    login_page_settings = LoginPageSettings.objects.first()

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('GymFreak')
        else:
            messages.error(request, 'Invalid login credentials. Please try again.')

    return render(request, 'login/index.html', {'login_page_settings': login_page_settings})

def custom_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('loginn')
    return redirect('loginn')


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully. Please log in.')
            return redirect('loginn')
    else:
        form = CustomUserCreationForm()

    login_page_settings = LoginPageSettings.objects.first()
    return render(request, 'signup/index.html', {'login_page_settings': login_page_settings, 'form': form})

def custom_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('loginn')
    return redirect('loginn')

# @login_required
def blog(request):
    return render(request, 'Blog/index.html')

def BookStore(request):
    categories = bookstore.objects.values_list('category', flat=True).distinct()

    allProds = []
    for category in categories:
        products = bookstore.objects.filter(category=category)
        range_values = range(products.count())
        nSlides = nSlides = (len(products) // 4) + ceil((len(products) / 4) - (len(products) // 4))
        allProds.append((products, range_values, nSlides))

    return render(request, 'BookStore/index.html', {'allProds': allProds})

def BookView(request, myid):
    book = BookView.objects.filter(id=myid)
    return render(request, 'BookStore/bookview.html', {'product': book[0]})