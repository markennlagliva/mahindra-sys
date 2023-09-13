from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('administrator/', views.administrator, name='administrator'),
    path('employee/', views.employee, name='employee'),

    # path for admin page SUCCESS
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('employee_dashboard/', views.employee_dashboard, name='employee_dashboard'),

    # logout and delete
    path('logout/', views.logoutUser, name='logoutUser'),
    path('delete_employee/<str:pk>/', views.delete_employee, name='delete_employee'),

    # ADMIN DASHBOARD
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('register_admin/', views.register_admin, name='register_admin'),
    path('register_employee/', views.register_employee, name='register_employee'),
    path('search_employee/', views.search_employee, name='search_employee'),

    # EMPLOYEE DASHBOARD
    path('employee_edit_profile/', views.employee_edit_profile, name='employee_edit_profile'),
    path('face_recognition', views.face_recognition, name='face_recognition')
]