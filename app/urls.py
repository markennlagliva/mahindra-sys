from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('administrator/', views.administrator, name='administrator'),
    path('employee/', views.employee, name='employee'),
]