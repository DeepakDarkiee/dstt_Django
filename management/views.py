
from django.shortcuts import render
from django.shortcuts import render,HttpResponse
from django.views import generic
from .models import Policy
from django.views.generic import TemplateView,CreateView,ListView

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
    success_url = ('/management/policy')

class PolicyListView(generic.ListView):
    model = Policy
    template_name = "management/policies.html"
    context_object_name = "policy"
# --------------------------------- Policy end ----------------------------------
