from django.urls import path
from . import views

urlpatterns = [
    path('employee/',views.AllEmployeeView.as_view(),name='employee' ),
    path('holiday/',views.HolidayView.as_view(),name='holiday' ),
    path('leaves_admin/',views.LeavesAdminView.as_view(),name='leaves_admin' ),
    path('leaves_employee/',views.LeavesEmployeeView.as_view(),name='leaves_employee' ),
    path('leaves_settings/',views.LeavesSettingsView.as_view(),name='leaves_settings' ),
    path('attendance_admin/',views.AttendanceAdminView.as_view(),name='attendance_admin' ),
    path('attendance_employee/',views.AttendanceEmployeeView.as_view(),name='attendance_employee' ),
    path('departments/',views.DepatmentsView.as_view(),name='departments' ),
    path('designations/',views.DesignationsView.as_view(),name='designations' ),
    path('timesheet/',views.TimesheetView.as_view(),name='timesheet' ),
    path('overtime/',views.OvertimeView.as_view(),name='overtime' ),
    
]