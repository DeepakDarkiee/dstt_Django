from django.shortcuts import render
from django.shortcuts import render,HttpResponse
from django.views import generic
from django.views.generic import TemplateView

# Create your views here.
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

