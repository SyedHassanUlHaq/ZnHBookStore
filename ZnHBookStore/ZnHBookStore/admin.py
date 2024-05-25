from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import bookstore, LoginPageSettings

admin.site.register(bookstore)
admin.site.register(LoginPageSettings)
