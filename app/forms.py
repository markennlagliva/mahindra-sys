from django import forms
from .models import Admin, Employee

class AdminInput(forms.ModelForm):
    class Meta:
        model = Admin
        fields = "__all__"

class EmployeeInput(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"


#Registration DB