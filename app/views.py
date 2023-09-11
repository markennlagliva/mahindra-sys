from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib import messages
from .models import ExtendUser

#restriction
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request, 'base.html')

def administrator(request):
     #Authentication Here... Pull data from DB
    if request.user.is_authenticated:
        return redirect('admin_dashboard')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('admin_dashboard')
            else:
                messages.info(request, 'Username or Password is incorrect...')
        
        context = {}
        return render(request, 'administrator.html', context)
   

def employee(request):

    #Authentication Here... Pull data from DB
    if request.user.is_authenticated:
        return redirect('employee_dashboard')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('employee_dashboard')
            else:
                messages.info(request, 'Username or Password is incorrect...')
    
        return render(request, 'employee.html')

    

# ADMIN DASHBOARD
@login_required(login_url='home')
def admin_dashboard(request):
    return render(request, 'admins/admin_dashboard.html')

@login_required(login_url='home')
def register_admin(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base.html')
    else:
        form = CreateUserForm()
    return render(request, 'admins/_register_admin.html', {'form': form})


@login_required(login_url='home')
def register_employee(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base.html')
    else:
        form = CreateUserForm()
    return render(request, 'admins/_register_employee.html', {'form': form})

@login_required(login_url='home')
def edit_profile(request):
    return render(request, 'admins/_edit_profile.html')


# EMPLOYEE DASHBOARD
@login_required(login_url='home')
def employee_dashboard(request):
    return render(request, 'employee/employee_dashboard.html', {})

#LOGGING OUT
@login_required(login_url='home')
def logoutUser(request):
    logout(request)
    return redirect('home')

