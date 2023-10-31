from django.shortcuts import render
from django.http import HttpResponse

def handler404(request, exception):
    return render(request, 'forbidden/404.html', {})

# def handler403(request, exception):
#     return HttpResponse('<h1>Forbidden</h1>')