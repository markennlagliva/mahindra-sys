from django import forms
from .models import AdminRegister, EmployeeRegister

class RegisteredAdmin(forms.ModelForm):
    class Meta:
        model = AdminRegister
        fields = "__all__"

class RegisteredEmployee(forms.ModelForm):
    class Meta:
        model = EmployeeRegister
        fields = "__all__"

#Registration DB