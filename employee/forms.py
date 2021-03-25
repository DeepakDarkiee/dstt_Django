from django import forms

from .models import Employee,Department,Designation,Holiday,AddLeave
class  EmployeeForm(forms.Form):
    employee_first_name = forms.CharField(max_length=30, required=False, help_text='Optional') 
    employee_last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    employee_email = forms.EmailField(max_length=30, required=False, help_text='Optional')
    employee_joining_date = forms.DateField()
    employee_department = forms.CharField(max_length=30, required=False, help_text='Optional')
    employee_id = forms.CharField(max_length=30, required=False, help_text='Optional')
    employee_phone = forms.CharField(max_length=30, required=False, help_text='Optional')
    employee_password = forms.CharField(max_length=30, required=False, help_text='Optional')
    employee_confirm_password = forms.CharField(max_length=30, required=False, help_text='Optional')
# --------------------------------------------Department------------------------------------------
class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = "__all__"
# --------------------------------------------Department------------------------------------------
# --------------------------------------------designation------------------------------------------
class DesignationForm(forms.ModelForm):
    class Meta:
        model = Designation
        fields = "__all__"
# --------------------------------------------/designation------------------------------------------

class HolidayForm(forms.ModelForm):
    class Meta:
        model = Holiday
        fields = "__all__"  

# -----------------------------------------Addleave---------------------------------------------------

class LeaveForm(forms.ModelForm):
    class Meta:
        model= AddLeave
        widgets = {
            'Leave_From' : forms.DateInput(attrs={'type':'date'}),
            'Leave_To' : forms.DateInput(attrs={'type':'date'})
        }
        fields = "__all__"
# -------------------------------------/addleave---------------------------------------------- 