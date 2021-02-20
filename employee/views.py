from django.contrib.auth.models import Group
from account.models import User
from django.shortcuts import  redirect
from django.views import generic
from django.views.generic import View,TemplateView,CreateView,UpdateView
from .models import Employee
from django.db import IntegrityError
from django.contrib import messages
from django.shortcuts import render,HttpResponse
from django.views import generic
from django.views.generic import TemplateView,CreateView,ListView
from .models import Employee,Department,Designation
from .forms import DepartmentForm,DesignationForm
from .forms import EmployeeForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
# Create your views here.


class EmployeeDashboardView(TemplateView):
    template_name = "employee/employee_dashboard.html"

def Employee_Profile(request):
    return render(request,"employee/employee_profile.html")

class HolidayView(TemplateView):
    template_name = "employee/holidays.html"

class LeavesAdminView(TemplateView):
    template_name = "employee/leaves_admin.html"

class LeavesEmployeeView(TemplateView):
    template_name = "employee/leaves_employee.html"

class LeavesSettingsView(TemplateView):
    template_name = "employee/leaves_settings.html"

class AttendanceAdminView(TemplateView):
    template_name = "employee/attendance_admin.html"

class AttendanceEmployeeView(TemplateView):
    template_name = "employee/attendance_employee.html"
# ----------------------------------------Department----------------------------------------------------------------------------------
class DepartmentCreateView(generic.CreateView):
    model = Department
    fields = ('department_department_name')
    template_name = "employee/departments.html"
    success_url = ('/employee/departments')
# ----------------------------------------Department----------------------------------------------------------------------------------

# ----------------------------------------/Department----------------------------------------------------------------------------------
class DesignationCreateView(generic.CreateView):
    model = Designation
    fields = ('designation_name', 'department_name')
    template_name = "employee/designations.html"
    success_url = ('/employee/designations_list')

class DesignationListView(generic.ListView): 
    model = Designation   
    template_name = "employee/designations.html" 
    context_object_name = "designations_list"
    # success_url = ('/employee/designations_list')

# ----------------------------------------Department----------------------------------------------------------------------------------

class TimesheetView(TemplateView):
    template_name = "employee/timesheet.html"

class OvertimeView(TemplateView):
    template_name = "employee/overtime.html"

