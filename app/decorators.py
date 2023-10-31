from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import logout


from django.contrib.auth.models import User


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None

            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
                print('This is the Group: ', group)
                print(type(group))
                usr = User.objects.get(username=request.user)
                user_groups = usr.groups.all()
                group_names = [user_perm for user_perm in user_groups]
                # print(group_names)
                # print('DS', type(str(group_names[0])))
                # print('DS-output:', str(group_names[0]))
                # # print(group_names[1])
                # print('user_groups len:', len(user_groups)) #same   
                # print('group_names len:', len(group_names)) #same
                if len(user_groups) == 2:
                    print('Inside if:', group_names)
                    return view_func(request, *args, **kwargs)
                elif group in allowed_roles:
                    return view_func(request, *args, **kwargs)
                else:
                    logout(request)
                    return render(request, 'forbidden/403.html' ,{'group' : group})
  
        return wrapper_func
    return decorator

def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'employee':
            return redirect('employee_dashboard')
        
        if group == 'admin':
            return view_func(request, *args, **kwargs)
        
    return wrapper_func

