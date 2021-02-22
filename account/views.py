# from groups_manager.models import Group,GroupType, Member
from account.models import User
from django.views.generic import TemplateView
from django.contrib.auth.models import  Group, Permission
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from employee.models import Employee
from django.conf import settings
from django.contrib.auth import authenticate, login ,logout
from django.http.response import HttpResponseRedirect
from django.shortcuts import render,HttpResponse,redirect
from django.urls import reverse_lazy
# from django.contrib.auth.models import Group, User
from django.views.generic import View,TemplateView,UpdateView
from django.db import IntegrityError
from django.contrib import messages
from django.contrib.contenttypes.models import ContentType




# Signs Up View

class SignInView(View):
    def post(self,request):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                if user.groups.all().exists() or user.is_superuser or user.is_admin:
                    return HttpResponseRedirect('/administration/index')
                else:
                    return HttpResponse("This Is Employee")
            else:
                return HttpResponse("Inactive user.")
        else:
            return HttpResponseRedirect(settings.LOGIN_URL)
    def get(self,request):
        return render(request, "account/login.html")


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(settings.LOGIN_URL)

# Role
@method_decorator(user_passes_test(lambda u: u.is_superuser), name='post')
class RegisterRole(View):
    def post(self,request):
        role_name = request.POST['role']
        try:
            group= Group.objects.create(name=role_name)
            messages.success(request,f"{group} Created successfully")
        except IntegrityError as e:
            messages.error(request,"already exist")
        groups=Group.objects.all()
        return render(request, "account/role.html",{'groups':groups})
    def get(self,request):
        groups=Group.objects.all()
        return render(request, "account/role.html",{'groups':groups})
        

class RemoveRole(View):
    def get(self,request,name):
        try:
            groups=Group.objects.get(name=name)          
            groups.delete()
            messages.success(request,f"{groups} deleted successfully")

        except Group.DoesNotExist:
            messages.error(request,"Role already Deleted or Not Created")
        return HttpResponseRedirect('/role')     



class RolePermissionView(View):
    def get(self,request,name):
        role=Group.objects.get(name=name)          
        permissions = role.permissions.all()
        print(permissions)
        
        for permission in permissions:
            if permission.codename == 'view_employee':
                view_employee = 'True'
            else:   
                view_employee = 'False'

            if permission.codename == 'add_employee':
                add_employee = 'True'
            else:
                add_employee = 'False'

            if permission.codename == 'change_employee':
                change_employee = 'True'
            else:
                change_employee = 'False'
            if permission.codename == 'delete_employee':
                delete_employee = 'True'
            else:
                delete_employee = 'False'
        #______________employee end_________________________________________
        return render(request,'account/add_roles_permission.html',
        {'role':role,
        # 'add_employee':add_employee,
        # 'view_employee':view_employee,
        # 'change_employee':change_employee,
        # 'delete_employee':delete_employee

          })

    def post(self,request,name):
        role = Group.objects.get(name=name)
        # ----------------------Employees-----------------------
        view_employee=request.POST['view_employee']
        add_employee=request.POST['add_employee']
        change_employee=request.POST['change_employee']
        delete_employee=request.POST['delete_employee']
        
        content_type = ContentType.objects.get_for_model(Employee,for_concrete_model=False)
        employee_permision=Permission.objects.filter(content_type=content_type)
        for permission in employee_permision:
            if permission.codename == 'view_employee':
                if view_employee == 'True':
                    role.permissions.add(permission)
                else:
                    role.permissions.remove(permission)
            if permission.codename == 'add_employee':
                if add_employee == 'True':
                    role.permissions.add(permission)
                else:
                    role.permissions.remove(permission)
            if permission.codename == 'change_employee':
                if change_employee == 'True':
                    role.permissions.add(permission)
                else:
                    role.permissions.remove(permission)
            if permission.codename == 'delete_employee':
                if delete_employee == 'True':
                    role.permissions.add(permission)
                else:
                    role.permissions.remove(permission)
        messages.success(request,f'Successfully Granted Permission to {role}')
        #______________employee end_________________________________________
        return render(request,'account/add_roles_permission.html',
        {'role':role,
        'view_employee':view_employee,
        'add_employee':add_employee,
        'change_employee':change_employee,
        'delete_employee':delete_employee
        })

        
class demoview(TemplateView):
    template_name = "account/demo.html"  

    
class UserToRole(View):
    def get(self, request,name):
        role = Group.objects.get(name=name)
        employees = Employee.objects.all()
        role_user=User.objects.filter(groups__name=role)
        for user in role_user:
            user.is_admin=True
            user.save()
        return render(request,'account/usertorole.html',
        {'role':role,'employees':employees,'role_user':role_user
        })

    def post(self, request,name):
        role = Group.objects.get(name=name)
        employe = request.POST['employee']
        user = User.objects.get(email=employe)
        userIngroup=user.groups.all().exists()
        
        
        if userIngroup != True:
            user.groups.add(role)
            messages.info(request,f"Congratulation {user} become a {role} ")
        else:
            userInWhichgroup=user.groups.all()
            for  userRole in userInWhichgroup:
                 messages.warning(request,f"Sorry {user} is Already having {userRole} Role ")
        return redirect('/usertorole/'+str(role))

class RemoveUserToRole(View):
    def get(self, request,name,id):
        role = Group.objects.get(name=name)
        user = User.objects.get(id=id)
        user.is_admin=False
        user.save()
        user.groups.remove(role)
        messages.warning(request,f"{user} is removed from {role} ")  
        return redirect('/usertorole/'+str(role))  

#

# def autocomplete(request):
#     if 'term' in request.GET:
#         qr=request.GET.get('term')
#         print(qr)
#         qs = Employee.objects.filter(employee_email__icontains=qr)
#         print(qs)
#         employee = list()
#         for q in qs:
#             employee.append(q.employee_email)
#         return JsonResponse(employee,safe=False)
#     return render(request,'demo.html')
