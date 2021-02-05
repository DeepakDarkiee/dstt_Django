from django import forms
from .models import Employee
class  EmployeeForm(forms.Form):
    employee_first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    employee_last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    employee_username = forms.CharField(max_length=30, required=False, help_text='Optional')
    employee_email = forms.EmailField(max_length=30, required=False, help_text='Optional')
    employee_joining_date = forms.DateField()
    employee_department = forms.CharField(max_length=30, required=False, help_text='Optional')
    employee_id = forms.CharField(max_length=30, required=False, help_text='Optional')
    employee_phone = forms.CharField(max_length=30, required=False, help_text='Optional')
    employee_password = forms.CharField(max_length=30, required=False, help_text='Optional')
    employee_confirm_password = forms.CharField(max_length=30, required=False, help_text='Optional')


    

    