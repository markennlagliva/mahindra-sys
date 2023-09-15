from django import forms
from .models import ExtendUser

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ExtendUserForm(forms.ModelForm):
    class Meta:
        model = ExtendUser
        fields = ['userid', 'age', 'gender', 'address', 'department', 'occupation']



class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']

        