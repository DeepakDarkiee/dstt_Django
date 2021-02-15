# from groups_manager.models import Group,GroupType, Member

from django.contrib.auth.models import  Group, Permission
from django.contrib.auth import models
from employee.models import Employee
from django.conf import settings
from django.contrib.auth import authenticate, login ,logout
from django.http.response import HttpResponseRedirect, HttpResponseRedirectBase
from django.shortcuts import redirect, render,HttpResponse
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
                return HttpResponseRedirect('/administration/index')
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
#
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
            # messages.success(request,f"{groups} deleted successfully")
        return render(request,'account/add_roles_permission.html',
        {'role':role,
        })
        
    def post(self,request,name):
        role = Group.objects.get(name=name)

        # ----------------------Employees-----------------------
        employee_access_module=request.POST['employee_module']
        
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
        
        permissions = role.permissions.all()
        for permission in permissions:
            if permission.codename == 'view_employee':
                view_employee = True
            if permission.codename == 'add_employee':
                add_employee = True
            if permission.codename == 'change_employee':
                change_employee = True
            if permission.codename == 'delete_employee':
                delete_employee = True
        #______________employee end_________________________________________
        return render(request,'account/add_roles_permission.html',
        {'role':role,
        'view_employee':view_employee,
        'add_employee':add_employee,
        'change_employee':change_employee,
        'delete_employee':delete_employee
        })

        
