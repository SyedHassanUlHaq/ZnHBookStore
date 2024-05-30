from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse    
import json
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import LoginPageSettings, BookStore, Orders, OrderUpdate, Contact
from math import ceil
MERCHANT_KEY = 'Your-Merchant-Key-Here'

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
            return redirect('profile/index.html')
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

@login_required
def index(request):
    updates = OrderUpdate.objects.all()
    context = {
        'updates': updates,
    }
    return render(request, 'profile/index.html', context)

@login_required
def blog(request):
    return render(request, 'Blog/index.html')

@login_required
def BookStoreView(request):
    categories = BookStore.objects.values_list('category', flat=True).distinct()

    allProds = []           # This code will not be executed
    for category in categories:
        products = BookStore.objects.filter(category=category)
        n = len(products)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append((products, range(1, nSlides), nSlides))

    return render(request, 'BookStore/index.html', {'allProds': allProds})

@login_required
def BookView(request, book_id):
    book = get_object_or_404(BookStore, book_id=book_id)
    return render(request, 'BookStore/bookview.html', {'product': book})

@login_required
def checkout(request):
    if request.method=="POST":
        return render(request, 'order/order.html')

    return render(request, 'checkout/checkout.html')

@login_required
def tracker(request):
    if request.method=="POST":
        orderId = request.POST.get('orderId', '')
        email = request.POST.get('email', '')
        try:
            order = Orders.objects.filter(order_id=orderId, email=email)
            if len(order)>0:
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps({"status":"success", "updates": updates, "itemsJson": order[0].items_json}, default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{"status":"noitem"}')
        except Exception as e:
            return HttpResponse('{"status":"error"}')

    return render(request, 'tracker/tracker.html')

# @login_required
# def handlerequest(request):
#     # paytm will send you post request here
#     form = request.POST
#     response_dict = {}
#     for i in form.keys():
#         response_dict[i] = form[i]
#         if i == 'CHECKSUMHASH':
#             checksum = form[i]

#     verify = Checksum.verify_checksum(response_dict, MERCHANT_KEY, checksum)
#     if verify:
#         if response_dict['RESPCODE'] == '01':
#             print('order successful')
#         else:
#             print('order was not successful because' + response_dict['RESPMSG'])
#     return render(request, 'paymentstatus/paymentstatus.html', {'response': response_dict})

@login_required
def profile(request):
    user = request.user

    return render(request, "profile/index.html")

@login_required
def contact(request):
    thank = False
    if request.method=="POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        thank = True
    return render(request, 'contact/index.html', {'thank': thank})