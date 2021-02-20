from django.http.response import HttpResponseRedirect
from django.shortcuts import render,HttpResponse,redirect
from django.urls.base import reverse
from django.views import generic
from django.views.generic import TemplateView,CreateView,ListView
from django.views.generic.base import View
from .models import Client,Asset,Lead
from .forms import ClientForm,AssetForm,LeadForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.contrib import messages
from employee.models import Employee
from account.models import User

# Create your views here.


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
                
                user = User.objects.create_user(email=employee_email,password=employee_password)
                user.is_staff=False
                user.full_name = employee_first_name+' '+employee_last_name
                user.is_active=True
                user.is_employee=True
                user.save()
                register_employee = Employee(user=user,employee_first_name=employee_first_name,employee_last_name=employee_last_name,employee_email=employee_email,employee_joining_date=employee_joining_date,employee_department=employee_department,employee_id=employee_id,employee_phone=employee_phone)
                register_employee.save()
                messages.success(request,"Employee Registered Successfully!")
            except IntegrityError as e:
                messages.error(request,"Email Already Registered!")
            
            
            return redirect('/administration/all_employee')
    else:
        groups=Group.objects.all()
        return render(request,'administration/employees.html',{'groups':groups})
            

def All_Employee_View(request):
    employee = Employee(request.GET)
    AllEmployee = Employee.objects.all()
    print(AllEmployee)
    return render(request,'administration/employees.html',{'Employee':AllEmployee})


def Update_Employees_View(request,id):
    employee_update = Employee.objects.get(id=id)  
    if request.method == "POST":
        employee_update.employee_department = request.POST.get('employee_department','')
        employee_update.employee_designation = request.POST.get('employee_designation','')
        employee_update.employee_phone = request.POST.get('employee_phone','')
        employee_update.employee_address = request.POST.get('employee_address','')
        employee_update.employee_state = request.POST.get('employee_state','')
        employee_update.employee_country = request.POST.get('employee_country','')
        employee_update.employee_pincode = request.POST.get('employee_pincode','')
        employee_update.employee_gender = request.POST.get('employee_gender','')
        employee_update.employee_birth_date = request.POST.get('employee_birth_date','')
        employee_update.employee_reports_to = request.POST.get('employee_reports_to','')
        if "employee_image" in request.FILES:
            img=request.FILES["employee_image"]
            employee_update.employee_image =img
            print (img)
        employee_update.save()
        # return HttpResponse("done")
    return render(request,"administration/employee_profile.html",{'employee_update':employee_update})
# ------------------------all employees for Administration ------------------------

class IndexView(TemplateView):
    template_name = "administration/index.html"

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
        messages.success(request,'deleted successfully')
        return HttpResponseRedirect('/administration/clients_list') 

class ClientRemoveGrid(View):
    def get(self,request,id):
        client=Client.objects.get(id=id)          
        client.delete()
        messages.success(request,'deleted successfully')
        return HttpResponseRedirect('/administration/clients_grid') 

# -----------------------------------/client----------------------------------------------------------------
  
# -------------------------------------Lead----------------------------------------------------------------
class CreateLeadView(generic.CreateView):
    model = Lead
    fields = ('lead_name', 'lead_email', 'lead_phone', 'lead_project', 'lead_assign_staff', 'lead_created', 'lead_status')
    template_name = "administration/leads.html" 
    success_url = ('/administration/leads_list')

class CreateLeadListView(generic.ListView):
    model = Lead
    template_name = "administration/leads.html"
    context_object_name = "lead_list"
    success_url = ('/administration/leads')
# ---------------------------------------/Lead----------------------------------------------------------------

class projectsView(TemplateView):
    template_name = "administration/projects.html"   
 
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
        return HttpResponseRedirect('/administration/asset_list'    )                      
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

class LeaveTypeView(TemplateView):
    template_name = "administration/setting_leave_type.html" 
   