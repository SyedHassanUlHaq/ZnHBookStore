from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse    
import json
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import LoginPageSettings, BookStore, Orders, OrderUpdate, Contact
from math import ceil
import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)

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
            return render(request, 'profile/index.html')
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
    # Fetch all orders
    orders = Orders.objects.all()

    # Get the currently logged-in user
    user = request.user

    # Create a dictionary to store orders and their updates
    orders_with_updates = {}

    # Loop through each order and fetch its updates
    for order in orders:
        updates = OrderUpdate.objects.filter(order=order)
        orders_with_updates[order] = updates

    context = {
        'user_name': user.username,
        'user_email': user.email,
        'user_contact': user.contact_number,  # Assuming you have this field in your CustomUser model
        'orders_with_updates': orders_with_updates,
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
        items_json = request.POST.get('itemsJson', '')
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        address = request.POST.get('address1', '') + " " + request.POST.get('address2', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        order = Orders(items_json=items_json, name=name, email=email, address=address, city=city,
                       state=state, zip_code=zip_code, phone=phone)
        order.save()
        thank = True
        id = order.order_id
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

# # @login_required
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

# @login_required
# def profile(request):
#     user = request.user

#     return render(request, "profile/index.html")

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