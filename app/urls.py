from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('administrator/', views.administrator, name='administrator'),
    path('employee/', views.employee, name='employee'),

    # path for admin page SUCCESS
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('employee_dashboard/', views.employee_dashboard, name='employee_dashboard'),

    # ADMIN DASHBOARD
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('register_admin/', views.register_admin, name='register_admin'),
    path('register_employee/', views.register_employee, name='register_employee'),
]