from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('administrator/', views.administrator, name='administrator'),
    path('employee/', views.employee, name='employee'),

    # path for admin page SUCCESS
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),

    path('register_admin/', views.registeradmin, name='register_admin'),
    path('register_employee/', views.registeremployee, name='register_employee'),
]