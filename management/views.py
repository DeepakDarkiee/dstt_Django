
from django.shortcuts import render
from django.shortcuts import render,HttpResponse
from django.views import generic
from .models import Policy
from django.views.generic import TemplateView,CreateView,ListView,UpdateView
from django.views.generic.base import View
from django.contrib import messages

# Create your views here.
class estimatesView(TemplateView):
    template_name = "management/estimates.html"

class estimatescreateView(TemplateView):
    template_name = "management/estimates_create.html"

class invoicesView(TemplateView):
    template_name = "management/invoices.html"

class invoicescreateView(TemplateView):
    template_name = "management/invoices_create.html"

class employeesalaryView(TemplateView):
    template_name = "management/employeesalary.html"

class employeepayslipView(TemplateView):
    template_name = "management/employeepayslip.html"

class employeepayrollitemsView(TemplateView):
    template_name = "management/employeepayroll_items.html"

class employeepoliciesView(TemplateView):
    template_name = "management/employeepolicies.html"

class employeeexpensereportView(TemplateView):
    template_name = "management/employeeexpense_report.html"

class invoicereportsView(TemplateView):
    template_name = "management/invoicereports.html"


# --------------------------------- Policy ----------------------------------
class PolicyCreateView(generic.CreateView):
    model = Policy
    fields = ('Policy_name', 'Policy_Description', 'Policy_Department', 'Policy_Upload_Policy',)
    template_name = "management/policies.html"
    success_url = ('/management/policy_list')

class PolicyListView(ListView):
    model = Policy
    # form_class = PolicyForm 
    template_name = "management/policies.html"
    context_object_name = "object_list" 


class PolicyManage(UpdateView):
    model = Policy
    context_object_name = "policy_update" 
    fields = ('Policy_name','Policy_Description','Policy_Department','Policy_Upload_Policy')
    template_name = "management/policies_manage.html"
    success_url = ('/management/policy_list/')


class PolicyRemove(View):
    def get(self,request,id):
        policy = Policy.objects.get(id=id)
        policy.delete()
        messages.success(request,"Deleted successfully") 
        return HttpResponseRedirect('/management/policy_list') 


# --------------------------------- Policy end ----------------------------------
