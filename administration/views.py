from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render,HttpResponse
from django.urls.base import reverse
from django.views import generic
from django.views.generic import TemplateView,CreateView,ListView
from django.views.generic.base import View
from .models import Client,Asset,Lead
from .forms import ClientForm,AssetForm,LeadForm
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.decorators import method_decorator

# Create your views here.

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

class LeadsRemove(View):
     def get(self,request,id):
        lead=Lead.objects.get(id=id)          
        lead.delete()
        messages.success(request,f"{lead} deleted successfully")
        return HttpResponseRedirect('/administration/leads_list') 

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
   