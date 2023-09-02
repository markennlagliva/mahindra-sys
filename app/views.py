from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'base.html')

def administrator(request):
    return render(request, 'child/administration.html')

def employee(request):
    return render(request, 'child/employee.html')