from django.contrib import admin
from .models import Employee,Department,Designation,Holiday,AddLeaveType,AddLeave
# Register your models here.



@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    class Meta:
        model = Employee
        fields = '__all__'
   
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    class Meta:
        model = Department
        fields = '__all__'

@admin.register(Designation)
class DesignationAdmin(admin.ModelAdmin):
    class Meta:
        model = Designation
        fields = '__all__'

@admin.register(Holiday)
class HolidayAdmin(admin.ModelAdmin):
    class Meta:
        model = Holiday
        fields = '__all__'

@admin.register(AddLeaveType)
class AddLeaveTypeAdmin(admin.ModelAdmin):
    class Meta:
        model = AddLeaveType
        fields = '__all__'

@admin.register(AddLeave)
class AddLeaveAdmin(admin.ModelAdmin):
    class Meta:
        model = AddLeave
        fields = '__all__'