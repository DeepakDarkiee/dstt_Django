from django.contrib import admin
from .models import Employee,Department,Designation,Holiday
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