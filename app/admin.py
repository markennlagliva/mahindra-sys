from django.contrib import admin
from .models import AdminRegister, EmployeeRegister
# Register your models here.

admin.site.register(AdminRegister)
admin.site.register(EmployeeRegister)



