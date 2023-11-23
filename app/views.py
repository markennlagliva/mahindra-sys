from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib import messages
from django.http import JsonResponse

#DATABASE and FORMS
from .models import ExtendUser # DATABASE HERE
from .forms import CreateUserForm, ExtendUserForm, CreateProfileForm
from django.contrib.auth.models import Group, User


# Filter
from .filters import ExtendUserFilter, AttendanceFilter

#restriction
from django.contrib.auth.decorators import login_required
from .decorators import allowed_users, admin_only

#Update password
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm


#FACE RECOGNITION 
from .utils import is_ajax, classify_face
import base64
from logs.models import Log, Attendance
from profiles.models import Profile 
from django.core.files.base import ContentFile





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
        form2 = CreateProfileForm(request.POST, request.FILES)
        if form.is_valid() and form1.is_valid() and form2.is_valid():
            user = form.save()
           
            username = form.cleaned_data.get('username')
            age = form1.cleaned_data.get('age')
            userid = form1.cleaned_data.get('userid')
            gender = form1.cleaned_data.get('gender')
            address = form1.cleaned_data.get('address')
            department = form1.cleaned_data.get('department')
            occupation = form1.cleaned_data.get('occupation')
            first_name = form1.cleaned_data.get('first_name')
            last_name = form1.cleaned_data.get('last_name')
            photo = form2.cleaned_data.get('photo')

            userdb = User.objects.get(username=username)
           
            obj = ExtendUser.objects.get(user=userdb.pk)
            obj.userid = userid
            obj.age = age
            obj.gender = gender
            obj.address = address 
            obj.department = department
            obj.occupation = occupation
            obj.first_name = first_name
            obj.last_name = last_name
            obj.save()

            group = Group.objects.get(name='admin')
            user.groups.add(group)

            obj_photo = Profile.objects.get(user=userdb.pk)
            print('This is the user:', obj_photo)
            obj_photo.photo = photo
            obj_photo.save()

            messages.success(request, 'Account was created for ADMIN ' + username)
            return redirect('register_admin')
    else:
        form = CreateUserForm()
        form1 = ExtendUserForm()
        form2 = CreateProfileForm()
    return render(request, 'admins/_register_admin.html', {'form': form, 'form1' : form1, 'form2' : form2})


@login_required(login_url='home')
@allowed_users(allowed_roles=['admin'])
@admin_only
def register_employee(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        form1 = ExtendUserForm(request.POST)
        form2 = CreateProfileForm(request.POST, request.FILES)
    
        if form.is_valid() and form1.is_valid() and form2.is_valid():
            user = form.save()
            # form2.save()

            username = form.cleaned_data.get('username')
            age = form1.cleaned_data.get('age')
            userid = form1.cleaned_data.get('userid')
            gender = form1.cleaned_data.get('gender')
            address = form1.cleaned_data.get('address')
            department = form1.cleaned_data.get('department')
            occupation = form1.cleaned_data.get('occupation')
            first_name = form1.cleaned_data.get('first_name')
            last_name = form1.cleaned_data.get('last_name')
            photo = form2.cleaned_data.get('photo')
            print('Thsis is the photo:', photo)
            userdb = User.objects.get(username=username)
           
            obj = ExtendUser.objects.get(user=userdb.pk)
           
            obj.userid = userid
            obj.age = age
            obj.gender = gender
            obj.address = address 
            obj.department = department
            obj.occupation = occupation
            obj.first_name = first_name
            obj.last_name = last_name
            obj.save()
            
            group = Group.objects.get(name='employee')
            user.groups.add(group)

            obj_photo = Profile.objects.get(user=userdb.pk)
            print('This is the user:', obj_photo)
            obj_photo.photo = photo
            obj_photo.save()

            messages.success(request, 'Account was created for EMPLOYEE ' + username)
        
            return redirect('register_employee')
    else:
        form = CreateUserForm()
        form1 = ExtendUserForm()
        form2 = CreateProfileForm()
    return render(request, 'admins/_register_employee.html', {'form': form, 'form1' : form1, 'form2' : form2})

@login_required(login_url='home')
@allowed_users(allowed_roles=['admin'])
@admin_only
def edit_profile(request):

    user = User.objects.get(username=request.user)

    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Update session to prevent logout
            messages.success(request, 'Your password ' + str(request.user) + ' was successfully changed.')
            return redirect('edit_profile')
    else:
        form = PasswordChangeForm(request.user)

    context = {'form' : form}
    return render(request, 'admins/_edit_profile.html', context)


@login_required(login_url='home')
@allowed_users(allowed_roles=['admin'])
@admin_only
def search_employee(request):
    #WORK RIGHT HERE......
    # DO AS WELL TO User DB to access name and lastname
    employee_info = ExtendUser.objects.all()
    users = User.objects.all()

    myFilter = ExtendUserFilter(request.GET, queryset=employee_info)  
    print(myFilter)
    for user in users:
        context = {'employees' : employee_info, 'user' : user, 'myFilter' : myFilter}
    return render(request, 'admins/_search_employee.html', context)

@login_required(login_url='home')
@allowed_users(allowed_roles=['admin'])
@admin_only
#Delete Employee 
def delete_employee(request, pk):
    
    # user = User.objects.get(pk=pk)
    users = ExtendUser.objects.get(user=pk)
    print(users, users.user.pk)
    user = User.objects.get(pk=users.user.pk)
    
    
    if request.method == "POST":
        user.delete()
        return redirect('search_employee')

    context = {'employee' : users}
    return render(request, 'admins/deleteEmployee.html', context)


#View Employee Attendance Records
def view_employee(request, first_name, last_name, pk):
    employee_info = ExtendUser.objects.get(first_name=first_name, last_name=last_name)
    print('This is pk:' ,employee_info.user.pk)
    user = User.objects.get(pk=employee_info.user.pk)
    print(user.username)
    #markenn work here

    
   
    # implement try and catch
    attendances = Attendance.objects.filter(employee_name=user.username)
    # perattendances = Attendance.objects.all()
    myFilter = AttendanceFilter(request.GET, queryset=attendances) 
  
    # print(str(myFilter.form))
  
  
    # for attendance in attendances:
    #     print(attendance.date)
    #     print(attendance.timein)
    #     print(attendance.timeout)
    #     print(attendance.total_hours)
    #     print(attendance.overtime)
    
    context = {'employee' : employee_info, 'attendances' : attendances, 'myFilter' : myFilter}
    return render(request, 'admins/_view.html', context)
    
    


# EMPLOYEE DASHBOARD
@login_required(login_url='home')
@allowed_users(allowed_roles=['employee'])
def employee_dashboard(request):
    return render(request, 'employee/employee_dashboard.html', {})

@login_required(login_url='home')
@allowed_users(allowed_roles=['employee'])
def employee_edit_profile(request):

    user = User.objects.get(username=request.user)

    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Update session to prevent logout
            messages.success(request, 'Your password ' + str(request.user) + ' was successfully changed.')
            return redirect('employee_edit_profile')
    else:
        form = PasswordChangeForm(request.user)


    context = {'form' : form}
    return render(request, 'employee/_employee.html', context)

@login_required(login_url='home')
@allowed_users(allowed_roles=['employee'])
def face_recognition(request):
    from datetime import datetime
    forDate = datetime.now()
    current_date = forDate.date() # For Date
    
    user_attendance_info = Attendance.objects.filter(employee_name=request.user, date__lte=current_date).order_by('-date')[:5]
    context = {'user_attendance_info': user_attendance_info}
    if is_ajax(request):
        
        photo = request.POST.get('photo')
        _, str_img = photo.split(';base64')

        decoded_file = base64.b64decode(str_img)

        x = Log()
        x.photo = ContentFile(decoded_file, 'upload.png')
        x.save()

        #classify the face
        res = classify_face(x.photo.path)
        user_exists = User.objects.filter(username=res).exists()
        print('result: ', res) #userade
        print('Does the face exist?: ', user_exists) #True
        
       
        from datetime import datetime
        currentDate = datetime.now()
        date = currentDate.date() # For Date
        time = currentDate.time() # For Time
        status = time.strftime('%p')
        # status = 'PM'
        if user_exists: #True
            
            def check(employee,date):
                if status == 'AM':
                    time_in = time.strftime('%H:%M:%S')
                    # time_in = '08:00:00'
                    formatted_time_12h = time.strftime('%I:%M %p') #render logic
                    # time_in = '8:00:00' #Example for Morning
                
                    obj_check = Attendance.objects.filter(employee_name=employee, date=date)
                    print('Total user log in Today:', len(obj_check))
                    print('This is AM')
                    if len(obj_check) > 1 or len(obj_check) == 1:
                        print('AM inside')
                        return JsonResponse({'success': 'Error'})
                    
                   
                    else:
                        import datetime
                        month = datetime.datetime.now().month
                        obj = Attendance(employee_name=employee, date=date, timein=time_in, month=month)
                        obj.save()  
                        return JsonResponse({'success': True})
                else:
                    time_out = time.strftime('%H:%M:%S')
                    formatted_time_12h = time.strftime('%I:%M %p') #render logic
                    print(formatted_time_12h)

                    obj_check = Attendance.objects.filter(employee_name=employee, date=date)

                    print('Total user log in Today:', len(obj_check))
                    obj_timeout = [data.timeout for data in obj_check]
                    
                    print('Type of len:', type(len(obj_check)))
                    print('This is the T or F:', len(obj_check) > 1)

                    if len(obj_check) > 1 or str(obj_timeout) != str('[datetime.time(0, 0)]'):
                        print('Inside if, we DID it!')
                        print('This is timeout', obj_timeout)
                        return JsonResponse({'success': 'Error'})
                    else:
                        condition = str(time_out).split(':')[0]
                        if int(condition) > 17:
                            attendance_instance = Attendance.objects.get(employee_name=employee, date=date)
                            attendance_instance.timeout = time_out
                            time_out_time = [x for x in time_out.split(':')]
                            time_in_time = [x for x in str(attendance_instance.timein).split(':')]
                            attendance_instance.total_hours = int(time_out_time[0]) - int(time_in_time[0]) - 1
                            if int(attendance_instance.total_hours) > 8:
                                attendance_instance.overtime = attendance_instance.total_hours - 8
                                attendance_instance.save()

                            attendance_instance.save()
                            return JsonResponse({'success': True})
                            
                        else:
                            attendance_instance = Attendance.objects.get(employee_name=employee, date=date)
                            print('This is else PM: ',attendance_instance.employee_name)
                            attendance_instance.timeout = time_out
                            time_out_time = [x for x in time_out.split(':')]
                            time_in_time = [x for x in str(attendance_instance.timein).split(':')]
                            attendance_instance.total_hours = int(time_out_time[0]) - int(time_in_time[0]) - 1
                            attendance_instance.overtime = 0
                            attendance_instance.save()
                            return JsonResponse({'success': True})
            res = check(res,date)
            return res
            # print(JsonResponse({'success': True}))
            # print('value of res:',res)
            # return JsonResponse({'success': True})
            
                
           
            # return HttpResponseRedirect(reverse('success'))
            # user = User.objects.get(username=res)
            # profile = Profile.objects.get(user=user)
            # print('user inside: ', user)
            # x.profile = profile
            # x.save()
        else: 
            print('Failed')    
            return JsonResponse({'success': False})

        
    else:
        print(user_attendance_info)
        return render(request, 'employee/_dailystatus.html', context)

@login_required(login_url='home')
@allowed_users(allowed_roles=['employee'])
def success(request):
    return render(request, 'employee/success.html', {})

@login_required(login_url='home')
@allowed_users(allowed_roles=['employee'])
def fail(request):
    return render(request, 'employee/fail.html', {})

@login_required(login_url='home')
@allowed_users(allowed_roles=['employee'])
def done(request):
    return render(request, 'employee/done.html', {})



#LOGGING OUT
@login_required(login_url='home')
def logoutUser(request):
    logout(request)
    return redirect('home')


