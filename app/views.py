from django.shortcuts import render, redirect
from .forms import AdminInput, EmployeeInput

# Create your views here.
def home(request):
    return render(request, 'base.html')

def administrator(request):
    #Authentication Here... Pull data from DB
    return render(request, 'administrator.html')
   

def employee(request):
    #Authentication Here... Pull data from DB
    return render(request, 'employee.html')


def adminpanel(request):
    return render(request, 'account/admin.html')

def register(request):
    if request.method == 'POST':
        form = AdminInput(request.POST)
        if form.is_valid():
            form.save()
            return redirect('base.html')
    else:
        form = AdminInput()
    return render(request, 'register.html', {'form': form})