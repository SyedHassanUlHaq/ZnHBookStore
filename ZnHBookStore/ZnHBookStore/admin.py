from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import BookStore, LoginPageSettings, Contact, OrderUpdate, Orders

admin.site.register(BookStore)
admin.site.register(LoginPageSettings)
admin.site.register(Contact)
admin.site.register(OrderUpdate)
admin.site.register(Orders)