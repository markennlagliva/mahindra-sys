from django import forms
from .models import AdminRegister, EmployeeRegister

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisteredAdmin(forms.ModelForm):
    class Meta:
        model = AdminRegister
        fields = "__all__"

class RegisteredEmployee(forms.ModelForm):
    class Meta:
        model = EmployeeRegister
        fields = "__all__"

#Registration DB

# class CreateUserForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = '__all__'