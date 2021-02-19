
from django.contrib.auth.models import Group
from account.models import User
from django.shortcuts import  redirect, render
from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView,CreateView
from .models import Employee
from django.db import IntegrityError
from django.contrib import messages

from django.shortcuts import  render
from django.shortcuts import render,HttpResponse
from django.views import generic
from django.views.generic import TemplateView,CreateView,ListView
from .models import Employee,Department,Designation
from .forms import DepartmentForm,DesignationForm
from .forms import EmployeeForm

from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def RegisterEmployeeView(request):
    if request.method =="POST":
            employee_first_name = request.POST['employee_first_name']
            employee_last_name = request.POST['employee_last_name']
            employee_email = request.POST['employee_email']
            employee_joining_date = request.POST['employee_joining_date']
            employee_department = request.POST['employee_department']
            employee_password = request.POST['employee_password']
            employee_confirm_password = request.POST['employee_confirm_password']
            employee_id = request.POST['employee_id']
            employee_phone = request.POST['employee_phone']
            employee_joining_date = request.POST['employee_joining_date']
            # employee_role = Group.objects.get(name=request.POST['employee_role'])
            try:
                
                user = User.objects.create_user(email=employee_email,password=employee_password)
                user.is_staff=False
                user.full_name = employee_first_name+' '+employee_last_name
                user.is_active=True
                user.is_employee=True
                user.save()
                register_employee = Employee(user=user,employee_first_name=employee_first_name,employee_last_name=employee_last_name,employee_email=employee_email,employee_joining_date=employee_joining_date,employee_department=employee_department,employee_id=employee_id,employee_phone=employee_phone)
                register_employee.save()
                messages.success(request,"Employee Registered Successfully!")
            except IntegrityError as e:
                messages.error(request,"Email Already Registered!")
            
            
            return redirect('/employee/RegisterEmployee')
    else:
        groups=Group.objects.all()
        return render(request,'employee/employee.html',{'groups':groups})
            
    
class AllEmployeeView(TemplateView):
    template_name = "employee/employee.html"

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

