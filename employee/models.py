
from django.db import models
from django.contrib.auth.models import Group
from account.models import User

# from django.contrib.auth.models import get_user_model

# -------------------------------Employee Model---------------------------------------------------------------------------------
from django.contrib.auth import get_user_model
User = get_user_model()
class Employee(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,default=True)
    employee_first_name=models.CharField(max_length=100)
    employee_last_name=models.CharField(max_length=100)
    employee_email=models.EmailField(max_length=100)
    employee_joining_date=models.CharField(max_length=50)
    employee_department=models.CharField(max_length=100)
    employee_designation =models.DateTimeField(auto_now=True)
    employee_id=models.CharField(max_length=100)
    employee_phone=models.CharField(max_length=100,null=True)
    employee_created_date=models.DateTimeField(auto_now=True)
    
    employee_birth_date=models.DateTimeField(auto_now=True,null=True)
    employee_gender=models.CharField(max_length=50,null=True)
    employee_address=models.CharField(max_length=50,null=True)
    employee_pin_code=models.CharField(max_length=50,null=True)
    employee_state=models.CharField(max_length=50,null=True)
    employee_country=models.CharField(max_length=50,null=True)
    employee_reports_to=models.CharField(max_length=50,null=True)
    employee_image=models.FileField()
    # Personal Informations 
    employee_passport_no=models.CharField(max_length=50,null=True)
    employee_passport_expiry_date=models.CharField(max_length=50,null=True)
    employee_tel=models.CharField(max_length=50,null=True)
    employee_nationality=models.CharField(max_length=50,null=True)
    employee_religion=models.CharField(max_length=50,null=True)
    employee_marital_status=models.CharField(max_length=50,null=True)
    employee_passport_no=models.CharField(max_length=50,null=True)
    employment_of_spouse=models.CharField(max_length=50,null=True)
    employee_no_of_children=models.CharField(max_length=50,null=True)
 
    employee_emergency_primary_name=models.CharField(max_length=50,null=True)
    employee_emergency_primary_relationship=models.CharField(max_length=50,null=True)
    employee_emergency_primary_phone1=models.CharField(max_length=50,null=True)
    employee_emergency_primary_phone2=models.CharField(max_length=50,null=True)
    employee_emergency_secondary_name=models.CharField(max_length=50,null=True)
    employee_emergency_secondary_relationship=models.CharField(max_length=50,null=True)
    employee_emergency_secondary_phone1=models.CharField(max_length=50,null=True)
    employee_emergency_secondary_phone2=models.CharField(max_length=50,null=True)
    
    employee_family_member_name=models.CharField(max_length=50,null=True)
    employee_family_member_relationship=models.CharField(max_length=50,null=True)
    employee_family_member_date_of_birth =models.CharField(max_length=50,null=True)
    employee_family_member_phone=models.CharField(max_length=50,null=True)
    
    employee_education_institution=models.CharField(max_length=50,null=True)
    employee_education_subject=models.CharField(max_length=50,null=True)
    employee_education_starting_date=models.CharField(max_length=50,null=True)
    employee_education_complete_date=models.CharField(max_length=50,null=True)
    employee_education_complete_date=models.CharField(max_length=50,null=True)
    employee_education_complete_date=models.CharField(max_length=50,null=True)
   
    employee_experience_company_name=models.CharField(max_length=50,null=True)
    employee_experience_company_location=models.CharField(max_length=50,null=True)
    employee_experience_company_job_position=models.CharField(max_length=50,null=True)
    employee_experience_company_period_from=models.CharField(max_length=50,null=True)
    employee_experience_company_period_to=models.CharField(max_length=50,null=True)



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
    Designation_Name = models.CharField(max_length=100)
    Department_Name=models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__(self):
        return self.designation_name
#------------------------------------/Designation------------------------------------------------------------