from django.shortcuts import render
from django.shortcuts import render,HttpResponse
from django.views import generic

from django.views.generic import TemplateView

# Create your views here.
class IndexView(TemplateView):
    template_name = "administration/index.html"

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
   