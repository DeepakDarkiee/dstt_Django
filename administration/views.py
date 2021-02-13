from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render,HttpResponse
from django.urls.base import reverse
from django.views import generic
from django.views.generic import TemplateView,CreateView,ListView
from .models import Client
from .forms import ClientForm
from django.urls import reverse_lazy

# Create your views here.

class IndexView(TemplateView):
    template_name = "administration/index.html"
# ------------------------client-----------------------------------------
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

# ------------------------client end--------------------------------------
  

class LeadsView(TemplateView):
    template_name = "administration/leads.html"  

class projectsView(TemplateView):
    template_name = "administration/projects.html"   
 
class taskboardView(TemplateView):
    template_name = "administration/taskboard.html"  

class assetsView(TemplateView):
    template_name = "administration/assets.html" 

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
   