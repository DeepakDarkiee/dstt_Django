from django.conf import settings
from django.contrib.auth import authenticate, login ,logout
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render,HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.models import Group, User
from django.views.generic import View,TemplateView,UpdateView
from django.db import IntegrityError
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

# Sign Up View
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

class RolePermissionView(TemplateView):
    template_name = "account/add_roles_permission.html"

# Roles
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

class ManageRole(View):
    def get(self,request,name):
        groups=Group.objects.get(name=name)
        groups.update('groups')
        messages.success(request,f"{groups} updated successfully")
        return HttpResponseRedirect('/role')
    
            
       
           