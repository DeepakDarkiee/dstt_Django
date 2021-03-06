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
    
    path('policy/',views.PolicyCreateView.as_view(),name='policy'),
    path('policy_list/',views.PolicyListView.as_view(),name='policy_list'),
    path('policy_remove/<int:id>',views.PolicyRemove.as_view(),name='policy_remove'),
    path('policy_manage/<int:pk>',views.PolicyManage.as_view(),name="policy_manage"),
    
    
]