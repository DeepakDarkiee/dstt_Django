from django.urls import path
from . import views

urlpatterns = [
    path('estimates/',views.estimatesView.as_view(),name='estimates'),
    path('estimatescreate/',views.estimatescreateView.as_view(),name='estimatescreate'),
    path('invoices/',views.invoicesView.as_view(),name='invoices'),
    path('invoicescreate/',views.invoicescreateView.as_view(),name='invoicescreate'),
    path('employeesalary/',views.employeesalaryView.as_view(),name='employeesalary'),
    path('employeepayslip/',views.employeepayslipView.as_view(),name='employeepayslip'),
    path('employeepayrollitems/',views.employeepayrollitemsView.as_view(),name='employeepayrollitems'),
    path('employeepolicies/',views.employeepoliciesView.as_view(),name='employeepolicies'),
    path('employeeexpensereport/',views.employeeexpensereportView.as_view(),name='employeeexpensereport'),
    path('invoicereports/',views.invoicereportsView.as_view(),name='invoicereports'),
    path('policies/',views.policiesView.as_view(),name='policies'),
    
]