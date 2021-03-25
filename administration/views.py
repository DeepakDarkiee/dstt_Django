from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.http.response import HttpResponseRedirect
from django.shortcuts import render,HttpResponse,redirect
from django.urls.base import reverse
from django.views import generic
from django.views.generic import TemplateView,CreateView,ListView,UpdateView
from django.views.generic.base import View
from .models import Client,Asset,Lead,Project
from .forms import ClientForm,AssetForm,LeadForm,ProjectForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.decorators import method_decorator
from employee.models import Employee,AddLeaveType
from django.db import IntegrityError
from account.models import User
import sweetify
# Create your views here.
from django.db.models import Q

# -------------------------------------all employee for admin--------------------------------
@login_required
def Register_Employee_View(request):
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
            
            # employee_role = Group.objects.get(name=request.POST['employee_role'])
            try:
                if(employee_password==employee_confirm_password):
                    user = User.objects.create_user(email=employee_email,password=employee_password)
                    user.is_staff=False
                    user.full_name = employee_first_name+' '+employee_last_name
                    user.is_active=True
                    user.is_employee=True
                    user.save()
                    register_employee = Employee(user=user,employee_first_name=employee_first_name,employee_last_name=employee_last_name,employee_email=employee_email,employee_joining_date=employee_joining_date,employee_department=employee_department,employee_id=employee_id,employee_phone=employee_phone)
                    register_employee.save()
                    # messages.success(request,"Employee Registered Successfully!")
                    sweetify.success(request, 'Employee Registered Successfully!', button='Ok', timer=3000)

                else:
                    messages.error(request," Confirm password and password does not match!")
            except IntegrityError as e:
                messages.error(request,"Email Already Registered!")
            
            
            return redirect('/administration/all_employee')
    else:
        groups=Group.objects.all()
        return render(request,'administration/employees.html',{'groups':groups})
           
@login_required
def All_Employee_View(request):
    AllEmployee = Employee.objects.filter(employee_status="Active")
    return render(request,'administration/employees.html',{'Employees':AllEmployee})
           
@login_required
def All_Employee_List_View(request):
    AllEmployee = Employee.objects.filter(employee_status="Active")
    return render(request,'administration/employees_list.html',{'Employees':AllEmployee})

@login_required
def Remove_Employee(request,id):
    Employees = Employee.objects.get(id=id)
    print(Employees)
    Employees.delete()
    messages.success(request,"deleted successfully")
    return HttpResponseRedirect('/administration/all_employee') 


@login_required
def Remove_Employee_List(request,id):
    Employees = Employee.objects.get(id=id)
    print(Employees)
    Employees.delete()
    messages.success(request,"deleted successfully")
    return HttpResponseRedirect('/administration/all_employee_list') 
    
@login_required
def Update_Employees_View(request,id):
    update_info = Employee.objects.get(id=id)
    return render(request,'administration/employee_profile.html',{'update_info':update_info})

# def Update_emergency_contact(request,id):
#     update_info = Employee.objects.get(id=id)
#     return render(request,'administration/employee_emergency_contact.html',{'update_info':update_info})

# def Update_faimly_information(request,id):
#     update_info = Employee.objects.get(id=id)
#     return render(request,'administration/employee_faimly_information.html',{'update_info':update_info})

# def Update_education_information(request,id):
#     update_info = Employee.objects.get(id=id)
#     return render(request,'administration/employee_education_information.html',{'update_info':update_info})



@login_required
def  Update_profile_info(request,id):
    update_info = Employee.objects.get(id=id)
    if request.method == "POST":
        update_info.employee_department = request.POST.get('employee_department','')
        update_info.employee_designation = request.POST.get('employee_designation','')
        update_info.employee_phone = request.POST.get('employee_phone','')
        update_info.employee_address = request.POST.get('employee_address','')
        update_info.employee_state = request.POST.get('employee_state','')
        update_info.employee_country = request.POST.get('employee_country','')
        update_info.employee_pin_code = request.POST.get('employee_pin_code','')
        update_info.employee_gender = request.POST.get('employee_gender','')
        update_info.employee_birth_date = request.POST.get('employee_birth_date','')
        update_info.employee_reports_to = request.POST.get('employee_reports_to','')
        update_info.employee_status = request.POST.get('employee_status','')
        if "employee_image" in request.FILES:
            img=request.FILES["employee_image"]
            update_info.employee_image =img
            print (img)
        update_info.save()
        return redirect("/administration/update_employees/"+str(id))
    return render(request,"administration/employee_profile_information.html",{'update_info':update_info})
@login_required
def Update_personal_info(request,id):
    update_info = Employee.objects.get(id=id) 
    print(update_info)
    if request.method == "POST":
        update_info.employee_passport_no = request.POST.get('employee_passport_no','')
        update_info.employee_passport_expiry_date = request.POST.get('employee_passport_expiry_date','')
        update_info.employee_tel = request.POST.get('employee_tel','')
        update_info.employee_nationality = request.POST.get('employee_nationality','')
        update_info.employee_religion = request.POST.get('employee_religion','')
        update_info.employee_marital_status = request.POST.get('employee_marital_status','')
        update_info.employee_passport_no = request.POST.get('employee_passport_no','')
        update_info.employment_of_spouse = request.POST.get('employment_of_spouse','')
        update_info.employee_no_of_children = request.POST.get('employee_no_of_children','')
        update_info.save()
        print(update_info)
        return redirect("/administration/update_employees/"+str(id))
    # update_info = Employee.objects.get(id=id)  
    return render(request,"administration/employee_personal_Information.html",{'update_info':update_info})


@login_required
def Update_emergency_information(request,id):
    update_info = Employee.objects.get(id=id)
    if request.method == "POST":
        update_info.employee_emergency_primary_name = request.POST.get('employee_emergency_primary_name','')
        update_info.employee_emergency_primary_relationship = request.POST.get('employee_emergency_primary_relationship','')
        update_info.employee_emergency_primary_phone1 = request.POST.get('employee_emergency_primary_phone1','')
        update_info.employee_emergency_primary_phone2 = request.POST.get('employee_emergency_primary_phone2','')
        update_info.employee_emergency_secondary_name = request.POST.get('employee_emergency_secondary_name','')
        update_info.employee_emergency_secondary_relationship = request.POST.get('employee_emergency_secondary_relationship','')
        update_info.employee_emergency_secondary_phone1 = request.POST.get('employee_emergency_secondary_phone1','')
        update_info.employee_emergency_secondary_phone2 = request.POST.get('employee_emergency_secondary_phone2','')
        update_info.save()
        print(update_info)
        return redirect("/administration/update_employees/"+str(id))
    return render(request,'administration/employee_emergency_contact.html',{'update_info':update_info})    

@login_required
def Update_faimly_information(request,id):
    update_info = Employee.objects.get(id=id)
    if request.method == "POST":
        update_info.employee_family_member_name = request.POST.get('employee_family_member_name','')
        update_info.employee_family_member_relationship = request.POST.get('employee_family_member_relationship','')
        update_info.employee_emergency_primary_phone1 = request.POST.get('employee_family_member_date_of_birth','')
        update_info.employee_emergency_primary_phone2 = request.POST.get('employee_family_member_phone','')
        update_info.save()
        print(update_info)
        return redirect("/administration/update_employees/"+str(id))
    return render(request,'administration/employee_faimly_information.html',{'update_info':update_info})  
@login_required
def Update_education_information(request,id):
    update_info = Employee.objects.get(id=id)
    if request.method == "POST":
        update_info.employee_education_institution = request.POST.get('employee_education_institution','')
        update_info.employee_education_subject = request.POST.get('employee_education_subject','')
        update_info.employee_education_starting_date = request.POST.get('employee_education_starting_date','')
        update_info.employee_education_complete_date = request.POST.get('employee_education_complete_date','')
        update_info.employee_education_degree = request.POST.get('employee_education_degree','')
        update_info.employee_education_grade = request.POST.get('employee_education_grade','')
        update_info.save()
        print(update_info)
        return redirect("/administration/update_employees/"+str(id))
    return render(request,'administration/employee_education_information.html',{'update_info':update_info})  

@login_required
def Update_experience_information(request,id):
    update_info = Employee.objects.get(id=id)
    if request.method == "POST":
        update_info.employee_experience_company_name = request.POST.get('employee_experience_company_name','')
        update_info.employee_experience_company_location = request.POST.get('employee_experience_company_location','')
        update_info.employee_experience_company_job_position = request.POST.get('employee_experience_company_job_position','')
        update_info.employee_experience_company_period_from = request.POST.get('employee_experience_company_period_from','')
        update_info.employee_experience_company_period_to = request.POST.get('employee_experience_company_period_to','')
        update_info.save()
        return redirect("/administration/update_employees/"+str(id))
    return render(request,'administration/employee_experience.html',{'update_info':update_info})

@login_required
def EditClient(request,id):
    edit_client = Client.objects.get(id=id) 
    print(edit_client.id)
    if request.method == "POST":
        edit_client.client_first_name = request.POST.get('client_first_name','')
        edit_client.client_last_name = request.POST.get('client_last_name','')
        edit_client.client_username =  request.POST.get('client_username','')
        edit_client.client_email = request.POST.get('client_email','')
        edit_client.client_id = request.POST.get('client_id','')
        edit_client.client_address = request.POST.get('client_address','')
        edit_client.client_phone = request.POST.get('client_phone','')
        edit_client.client_status = request.POST.get('client_status','')
        edit_client.save()
    return render(request,"administration/client_form.html",{'edit_client':edit_client})
class IndexView(TemplateView):
    template_name = "administration/index.html"

    @method_decorator(login_required(login_url='/'))
    def dispatch(self, *args, **kwargs):
        return super(IndexView, self).dispatch(*args, **kwargs)

 

# --------------------------------------------client------------------------------------------------------------------------
class CreateClientsView(generic.CreateView):
    model = Client
    tamplate_name = "administration/clients_form.html"
    fields = ('client_first_name', 'client_last_name', 'client_username', 'client_email', 'client_id', 'client_address', 'client_phone' )
    success_url = ('/administration/clients_grid')


class CreateClientsListView(generic.ListView):
    model = Client
    template_name = "administration/client_list.html" 
    context_object_name = "client_list"
    success_url = ('/administration/clients_list')

class CreateClientsGridView(generic.ListView):
    model = Client
    template_name = "administration/client_form.html" 
    context_object_name = "client_list"
    success_url = ('/administration/clients_grid')

class ClientRemove(View):
    def get(self,request,id):
        client=Client.objects.get(id=id)          
        client.delete()
        messages.success(request,'deleted successfuully')
        return HttpResponseRedirect('/administration/clients_list') 

class ClientRemoveGrid(View):
    def get(self,request,id):
        client=Client.objects.get(id=id)          
        client.delete()
        messages.success(request,'deleted successfuully')
        return HttpResponseRedirect('/administration/clients_grid')  


class ClientManageGrid(UpdateView):
    model = Client
    fields = ['client_first_name','client_last_name','client_username','client_email','client_id','client_address','client_phone','client_status']
    context_object_name = "client_update"
    template_name = "administration/client_grid_manage.html"             
    success_url = ("/administration/clients_grid/")    

class ClientManageList(UpdateView):
    model = Client
    fields = ['client_first_name','client_last_name','client_username','client_email','client_id','client_address','client_phone','client_status'] 
    context_object_name = "client_list_update"
    template_name = "administration/client_list_manage.html"
    success_url = ("/administration/clients_list/")
# -----------------------------------/client----------------------------------------------------------------
  
# -------------------------------------Lead----------------------------------------------------------------
class CreateLeadView(generic.CreateView):
    model = Lead
    fields = ('lead_name', 'lead_email', 'lead_phone', 'lead_project', 'lead_assign_staff', 'lead_created',)
    template_name = "administration/leads.html" 
    success_url = ('/administration/leads_list')

class CreateLeadListView(generic.ListView):
    model = Lead
    template_name = "administration/leads.html"
    context_object_name = "lead_list"
    success_url = ('/administration/leads')

class LeadsRemove(View):
     def get(self,request,id):
        lead=Lead.objects.get(id=id)          
        lead.delete()
        messages.success(request,f"{lead} deleted successfully")
        return HttpResponseRedirect('/administration/leads_list') 

class LeadManage(UpdateView):
    model = Lead
    fields = ['lead_name','lead_email','lead_phone','lead_project','lead_assign_staff','lead_created'] 
    context_object_name = "lead_update"
    template_name = "administration/lead_manage.html"
    success_url = ("/administration/leads_list/")

# ---------------------------------------/Lead----------------------------------------------------------------

#---------------------------------------project-------------------------------------------------------------------
class projectsView(View):
    model = Project
    fields = ['project_name','client','start_date','end_date','rate','rate_type','priority','add_project_leader','description','upload_files']
    template_name = "administration/projects.html"
    success_url = ("/administration/projects/")
 
class taskboardView(TemplateView):
    template_name = "administration/taskboard.html" 

# ----------------------------------Assets------------------------------------------------
class AssetCreateView(generic.CreateView):
    model = Asset
    fields = ('asset_name', 'asset_id', 'asset_purcahse_date', 'asset_purcahse_from', 'asset_manufacture', 'asset_model', 'asset_serial_number', 'asset_supplier', 'asset_conditiion', 'asset_warrenty', 'asset_amount', 'asset_user', 'asset_description', 'asset_status')
    template_name = "administration/assets.html" 
    success_url = ('/administration/asset_list')

class AssetListView(generic.ListView):
    model = Asset
    template_name = "administration/assets.html" 
    context_object_name = "asset_list"
    success_url = ('/administration/assets')

class AssetRemove(View):
     def get(self,request,id):
        asset=Asset.objects.get(id=id)          
        asset.delete()
        messages.success(request,f"{asset} deleted successfully")
        return HttpResponseRedirect('/administration/asset_list') 
                              
class AssetManage(View):
    def get(self,request,name):
        asset=Asset.objects.get(name=name)
        asset.update()
        messages.success(request,f"{asset} updated successfully")
        return HttpResponseRedirect('/administration/asset_list')                      
# ----------------------------------/Assets------------------------------------------------

class jobsView(TemplateView):
    template_name = "administration/jobs.html"  

class jobsapplicantsView(TemplateView):
    template_name = "administration/jobsapplicants.html"  

class knowledgebaseView(TemplateView):
    template_name = "administration/knowledgebase.html"  

class activitiesView(TemplateView):
    template_name = "administration/activities.html"  
   
class usersView(TemplateView):
    template_name = "administration/users.html"  

class settingsView(TemplateView):
    template_name = "administration/settings.html" 

class ticketView(TemplateView):
    template_name = "administration/ticket.html" 
   
class localizationView(TemplateView):
    template_name = "administration/localization.html" 
   
class SettingsThemeView(TemplateView):
    template_name = "administration/settings_theme.html" 

class RolePermissionsView(TemplateView):
    template_name = "administration/roles_permissions.html" 

class SettingEmailView(TemplateView):
    template_name = "administration/setting_email.html" 
   
class SettingInvoiceView(TemplateView):
    template_name = "administration/setting_invoice.html" 
   
class SettingSalaryView(TemplateView):
    template_name = "administration/setting_salary.html" 
   
class SettingNotificationView(TemplateView):
    template_name = "administration/setting_notifications.html" 
   
class ChangePasswordView(TemplateView):
    template_name = "administration/setting_change_password.html" 

class LeaveTypeView(generic.CreateView):
    model = AddLeaveType
    fields = ['Leave_Type','Number_of_days']
    template_name = "administration/setting_leave_type.html"
    success_url = ("/administration/leavetypelist/")
 
class LeaveTypeListView(generic.ListView):
    model = AddLeaveType
    template_name = "administration/setting_leave_type.html" 
    context_object_name = "leavetype_list"
    success_url = ('/administration/leavetypelist/')   

class LeaveTypeRemoveView(View):
    def get(self,request,id):
        Leave_Type=AddLeaveType.objects.get(id=id)          
        Leave_Type.delete()
        messages.success(request,f"{Leave_Type} deleted successfully")
        return HttpResponseRedirect('/administration/leavetypelist')

class LeaveTypeManageView(View):
    model = AddLeaveType
    fields = ['Leave_Type','Number_of_days']
    context_object_name = "LeaveType"
    template_name = "administration/settingleavetype_manage.html"             
    success_url = ("/administration/manageleavetype/")    