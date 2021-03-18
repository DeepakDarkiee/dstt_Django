from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.http.response import HttpResponseRedirect
from django.shortcuts import render,HttpResponse,redirect
from django.urls.base import reverse
from django.views import generic
from django.views.generic import TemplateView,CreateView,ListView,UpdateView
from django.views.generic.base import View
from .models import Client,Asset,Lead
from .forms import ClientForm,AssetForm,LeadForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.decorators import method_decorator
from employee.models import Employee
from django.db import IntegrityError
from account.models import User
import sweetify
# Create your views here.
from django.db.models import Q



class EmployeeSearchResultsView(ListView):
    model = Employee
    template_name ='administration/employees.html'
    context_object_name = "Employees"
    
    def get_queryset(self):
        email = self.request.GET.get('employee_email') # new
        name = self.request.GET.get('employee_name') # new
        Employees = Employee.objects.filter(
            Q(employee_email__icontains=email) | Q(employee_first_name__icontains=email)
        )
        return Employees
         