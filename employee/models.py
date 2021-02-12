
from django.db import models
from django.contrib.auth.models import Group
from account.models import User


# -------------------------------Employee Model---------------------------------------------------------------------------------
from django.contrib.auth import get_user_model
User = get_user_model()
class Employee(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,default=True)
    role = models.ForeignKey(Group, on_delete=models.CASCADE,default='Employee')
    employee_first_name=models.CharField(max_length=100)
    employee_last_name=models.CharField(max_length=100)
    employee_email=models.EmailField(max_length=100)
    employee_joining_date=models.DateField(null=True)
    employee_department=models.CharField(max_length=100)
    employee_id=models.CharField(max_length=100)
    employee_phone=models.CharField(max_length=100)
    employee_created_date=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.employee_email
# -------------------------------/Employee Model---------------------------------------------------------------------------------


#------------------------------------Depaartment------------------------------------------------------------
class Department(models.Model):
    department_name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.department_name
#------------------------------------/Depaartment------------------------------------------------------------
#------------------------------------Designation------------------------------------------------------------
class Designation(models.Model):
    designation_name = models.CharField(max_length=100)
    department_name=models.CharField(max_length=100)

    def __str__(self):
        return self.designation_name
#------------------------------------/Designation------------------------------------------------------------