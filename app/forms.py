from django import forms
from .models import ExtendUser
from profiles.models import Profile

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ExtendUserForm(forms.ModelForm):
    class Meta:
        model = ExtendUser
        fields = ['userid', 'age', 'gender', 'address', 'department', 'occupation', 'first_name', 'last_name']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['photo']

        