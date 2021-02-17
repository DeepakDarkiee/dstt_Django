from django.shortcuts import render
from django.shortcuts import render,HttpResponse
from django.views import generic
from django.views.generic import TemplateView

# Create your views here.

class IndexView(TemplateView):
    template_name = "administration/index.html"

class Employee(TemplateView):
    template_name = "administration/employee.html"

class ClientsView(TemplateView):
    template_name = "administration/clients.html"    

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
   