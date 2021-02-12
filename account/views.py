# from groups_manager.models import Group,GroupType, Member
from django.contrib.auth.models import Group
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
from django.core.exceptions import ObjectDoesNotExist



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
        return render(request, "account/add_roles_permission.html",{'role':role})
    def post(self,request,name):
        role = Group.objects.get(name=name)
        employee_module=request.POST['employee_module']
        employee_read=request.POST['employee_read']
        employee_write=request.POST['employee_write']
        employee_create=request.POST['employee_create']
        employee_delete=request.POST['employee_delete']
        return HttpResponse("Yes")
        # print(role,employee_module,employee_read,employee_write,employee_create,employee_delete)
        
# def group_manager(request):

#     # Create group types (optional)
#     organization = GroupType.objects.create(label='Organization')
#     division = GroupType.objects.create(label='Division')

#     # Organization A has 'commercials' and 'managers'
#     org_a = Group.objects.create(name='Org A, Inc.', group_type=organization)
#     org_a_commercials = Group.objects.create(name='Commercials', group_type=division, parent=org_a)
#     org_a_managers = Group.objects.create(name='Managers', group_type=division, parent=org_a)
#     # Tina is a commercial
#     tina = Member.objects.create(email='tina@gmail.com')
#     org_a_commercials.add_member(tina)
#     # Jack is a manager
#     jack = Member.objects.create(email='deepak@gmail.com')
#     org_a_managers.add_member(jack)
#     return  HttpResponse("Group True")