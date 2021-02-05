from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render
from django.shortcuts import render,HttpResponse
from django.views import generic
from django.views.generic import TemplateView,CreateView
from .models import Employee
from .forms import EmployeeForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def RegisterEmployeeView(request):
    if request.method =="POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee_first_name = form.cleaned_data['employee_first_name']
            employee_last_name = form.cleaned_data['employee_last_name']
            employee_username = form.cleaned_data['employee_username']
            employee_email = form.cleaned_data['employee_email']
            employee_joining_date = form.cleaned_data['employee_joining_date']
            employee_department = form.cleaned_data['employee_department']
            employee_password = form.cleaned_data['employee_password']
            employee_confirm_password = form.cleaned_data['employee_confirm_password']
            employee_id = form.cleaned_data['employee_id']
            employee_phone = form.cleaned_data['employee_phone']
            employee_joining_date = form.cleaned_data['employee_joining_date']
            user = User.objects.create_user(username=employee_email,password=employee_password,email=employee_email,first_name=employee_first_name,last_name=employee_last_name)
            user.is_staff=False
            user.is_active=True
            user.save()
            register_employee = Employee(user=user,employee_first_name=employee_first_name,employee_last_name=employee_last_name,employee_username=employee_username,employee_email=employee_email,employee_joining_date=employee_joining_date,employee_department=employee_department,employee_id=employee_id,employee_phone=employee_phone)
            register_employee.save()
            return HttpResponse("saved")
    else:
        form = EmployeeForm()
        return render(request,'employee/employee.html',{'form':form})
            
    
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

class DepatmentsView(TemplateView):
    template_name = "employee/departments.html"

class DesignationsView(TemplateView):
    template_name = "employee/designations.html"

class TimesheetView(TemplateView):
    template_name = "employee/timesheet.html"

class OvertimeView(TemplateView):
    template_name = "employee/overtime.html"

