from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import RegisteredAdmin
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.contrib import messages
from .models import AdminRegister, EmployeeRegister





# Create your views here.
def home(request):
    return render(request, 'base.html')

def administrator(request):
     #Authentication Here... Pull data from DB
    if request.method == "POST":
        id = request.POST["userid"]
        password = request.POST["password"]

        #CUSTOM AUTHENTICATION
        user = AdminRegister.objects.filter(userid=id)
        for record in user:
            verify = record.userid == int(id) and record.password == password
            if verify:
                return redirect('admin_dashboard')
            else:
                messages.success(request, ("There was an Error, Credentials may not be exist!"))
                return redirect('administrator')
    else:
        return render(request, 'administrator.html')
   

def employee(request):
    #Authentication Here... Pull data from DB
    if request.method == "POST":
        id = request.POST["userid"]
        password = request.POST["password"]

        #CUSTOM AUTHENTICATION
        user = EmployeeRegister.objects.filter(userid=id)
        for record in user:
            if record.userid == int(id) and record.password == password:
                return redirect('employee_dashboard')
            else:
                messages.success(request, ("There was an Error, Credentials may not be exist!"))
                return redirect('employee')
    else:
        return render(request, 'employee.html')

    


def admin_dashboard(request):
    return render(request, 'admins/admin_dashboard.html')

def employee_dashboard(request):
    return render(request, 'employee/employee_dashboard.html')

def registeradmin(request):
    if request.method == 'POST':
        form = RegisteredAdmin(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base.html')
    else:
        form = RegisteredAdmin()
    return render(request, 'register.html', {'form': form})

def registeremployee(request):
    pass