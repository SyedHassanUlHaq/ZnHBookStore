from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    profile_pic = forms.ImageField(required=False)
    email = forms.CharField(max_length=50, required=False)
    contact_number = forms.CharField(max_length=11, required=False)

    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('email', 'contact_number', 'profile_pic')