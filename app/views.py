from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import RegisteredAdmin
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'base.html')

def administrator(request):
    #Authentication Here... Pull data from DB
    if request.method == "POST":
        userid = request.POST["userid"]
        password = request.POST["password"]
        user = authenticate(request, userid=userid, password=password)

        if user:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            messages.success(request, ("There was an Error, Credentials may not be exist!"))
            return redirect('administrator')
    else:
        return render(request, 'administrator.html')
   

def employee(request):
    #Authentication Here... Pull data from DB
    return render(request, 'employee.html')


def admin_dashboard(request):
    return render(request, 'admins/admin_dashboard.html')

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