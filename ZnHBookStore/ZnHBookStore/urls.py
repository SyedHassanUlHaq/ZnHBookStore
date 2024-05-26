"""
URL configuration for ZnHBookStore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.profile, name='myprofile'),
    path('loginn/', views.loginn, name='loginn'),
    path('signup/', views.signup, name='signup'),
    path("Blog/", views.blog, name='Blog'),
    path('logout/', views.custom_logout, name='logout'),
    path("book/<int:myid>", views.BookView, name='book'),
    path("BookStore/", views.BookStore, name='BookStore'),
    path("checkout/", views.checkout, name="Checkout"),
    path("Tracker/", views.tracker, name="TrackingStatus"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
