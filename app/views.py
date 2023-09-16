from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib import messages

#DATABASE and FORMS
from .models import ExtendUser # DATABASE HERE
from .forms import CreateUserForm, ExtendUserForm
from django.contrib.auth.models import Group, User


# Filter
from .filters import ExtendUserFilter

#restriction
from django.contrib.auth.decorators import login_required
from .decorators import allowed_users, admin_only

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
@allowed_users(allowed_roles=['admin'])
@admin_only
def admin_dashboard(request):
    return render(request, 'admins/admin_dashboard.html')

@login_required(login_url='home')
@allowed_users(allowed_roles=['admin'])
@admin_only
def register_admin(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        form1 = ExtendUserForm(request.POST)
        if form.is_valid() and form1.is_valid():
            user = form.save()
            form1.save()

            username = form.cleaned_data.get('username')
            
            group = Group.objects.get(name='admin')
            user.groups.add(group)

            messages.success(request, 'Account was created for ADMIN ' + username)
            return redirect('register_admin')
    else:
        form = CreateUserForm()
        form1 = ExtendUserForm()
    return render(request, 'admins/_register_admin.html', {'form': form, 'form1' : form1})


@login_required(login_url='home')
@allowed_users(allowed_roles=['admin'])
@admin_only
def register_employee(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        form1 = ExtendUserForm(request.POST)
        if form.is_valid() and form1.is_valid():
            user = form.save()
            user1 = form1.save()

            username = form.cleaned_data.get('username')
            
            group = Group.objects.get(name='employee')
            user.groups.add(group)

            messages.success(request, 'Account was created for EMPLOYEE' + username)
        
            return redirect('home')
    else:
        form = CreateUserForm()
    return render(request, 'admins/_register_employee.html', {'form': form})

@login_required(login_url='home')
@allowed_users(allowed_roles=['admin'])
@admin_only
def edit_profile(request):
    return render(request, 'admins/_edit_profile.html')


@login_required(login_url='home')
@allowed_users(allowed_roles=['admin'])
@admin_only
def search_employee(request):
    #WORK RIGHT HERE......
    # DO AS WELL TO User DB to access name and lastname
    employee_info = ExtendUser.objects.all()
    users = User.objects.all()

    myFilter = ExtendUserFilter(request.GET, queryset=employee_info)  

    for user in users:
        context = {'employees' : employee_info, 'user' : user, 'myFilter' : myFilter}
    return render(request, 'admins/_search_employee.html', context)

@login_required(login_url='home')
@allowed_users(allowed_roles=['admin'])
@admin_only
#Delete Employee Record
def delete_employee(request, pk):
    employee_info = ExtendUser.objects.get(userid=pk)
    # user = User.objects.get(username=employee_info.user)

    if request.method == "POST":
        employee_info.delete()
        # user.delete()
        return redirect('search_employee')

    context = {'employee' : employee_info}
    return render(request, 'admins/deleteEmployee.html', context)
    


# EMPLOYEE DASHBOARD
@login_required(login_url='home')
@allowed_users(allowed_roles=['employee'])
def employee_dashboard(request):
    return render(request, 'employee/employee_dashboard.html', {})

@login_required(login_url='home')
@allowed_users(allowed_roles=['employee'])
def employee_edit_profile(request):
    return render(request, 'employee/_employee.html', {})

@login_required(login_url='home')
@allowed_users(allowed_roles=['employee'])
def face_recognition(request):
    return render(request, 'employee/_dailystatus.html', {})



#LOGGING OUT
@login_required(login_url='home')
def logoutUser(request):
    logout(request)
    return redirect('home')


