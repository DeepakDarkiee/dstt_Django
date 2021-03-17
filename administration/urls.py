from . import search
from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.IndexView.as_view(),name='index' ),
# ------------------------------Employees-----------------------------------------------------------------------#
    path('update_employees/<int:id>',views.Update_Employees_View,name='update_employees' ),
    path('Update_profile_info/<int:id>',views.Update_profile_info,name='Update_profile_info' ),
    path('Update_emergency_information/<int:id>',views.Update_emergency_information,name='Update_emergency_information' ),
    path('Update_faimly_information/<int:id>',views.Update_faimly_information,name='Update_faimly_information' ),
    path('Update_education_information/<int:id>',views.Update_education_information,name='Update_education_information' ),
    path('Update_experience_information/<int:id>',views.Update_experience_information,name='Update_experience_information' ),
    path('Update_personal_info/<int:id>',views.Update_personal_info,name='Update_personal_info' ),
    path('Remove_employee/<int:id>',views.Remove_Employee,name='Remove_employee'),
    # path('Update_emergency_info/<int:id>',views.Update_emergency_info,name='Update_emergency_info' ),
    # path('Update_family_info/<int:id>',views.Update_family_info,name='Update_family_info' ),
    # path('Update_education_info/<int:id>',views.Update_education_info,name='Update_education_info' ),
    path('all_employee/',views.All_Employee_View,name='all_employee' ),
    path('registeremployee/',views.Register_Employee_View,name='registeremployee' ),
    
# ------------------------------Employees-----------------------------------------------------------------------#


# ------------------------------client---------------------------------------------------------------------------
    path('clients/',views.CreateClientsView.as_view(),name='clients' ),
    path('editClient/<int:id>',views.EditClient,name='editClient'),
    path('clients_list/',views.CreateClientsListView.as_view(),name='clients_list' ),
    path('clients_grid/',views.CreateClientsGridView.as_view(),name='clients_grid' ),
    path('clients_remove/<int:id>',views.ClientRemove.as_view(),name='clients_remove' ),
    path('clients_remove_grid/<int:id>',views.ClientRemoveGrid.as_view(),name='clients_remove_grid' ),
    path('client_manage_grid/<int:pk>',views.ClientManageGrid.as_view(),name='client_manage_grid' ),
    path('client_manage_list/<int:pk>',views.ClientManageList.as_view(),name='client_manage_list' ),
# ------------------------------client--------------------------------------------------------------------------

# ------------------------------Lead---------------------------------------------------------------------------
    path('leads/',views.CreateLeadView.as_view(),name='leads' ),
    path('leads_list/',views.CreateLeadListView.as_view(),name='leads_list' ),
    path('leads_remove/<int:id>',views.LeadsRemove.as_view(),name='leads_remove' ),
    path('leads_manage/<int:pk>',views.LeadManage.as_view(),name='leads_manage' ),
# ------------------------------/Lead--------------------------------------------------------------------------

    path('projects/',views.projectsView.as_view(),name='projects' ),
    path('taskboard/',views.taskboardView.as_view(),name='taskboard' ),

# -----------------------------------Assets-----------------------------------------------------------------------
    path('assets/',views.AssetCreateView.as_view(),name='assets' ),
    path('asset_list/',views.AssetListView.as_view(),name='asset_list' ),
    path('asset_remove/<int:id>',views.AssetRemove.as_view(),name='asset_remove' ),
    path('asset_manage/<int:id>',views.AssetManage.as_view(),name='asset_manage' ),
# -----------------------------------/Assets-----------------------------------------------------------------------
    
    path('jobs/',views.jobsView.as_view(),name='jobs' ),
    path('jobsapplicants/',views.jobsapplicantsView.as_view(),name='jobsapplicants' ),
    path('knowledgebase/',views.knowledgebaseView.as_view(),name='knowledgebase' ),
    path('activities/',views.activitiesView.as_view(),name='activities' ),
    path('users/',views.usersView.as_view(),name='users' ),
    path('settings/',views.settingsView.as_view(),name='settings' ),
    path('ticket/',views.ticketView.as_view(),name='ticket'),
    path('localization/',views.localizationView.as_view(),name='localization'),
    path('settingtheme/',views.SettingsThemeView.as_view(),name='settingtheme'),
    path('rolepermissions/',views.RolePermissionsView.as_view(),name='rolepermissions'),
    path('settingemail/',views.SettingEmailView.as_view(),name='settingemail'),
    path('settinginvoice/',views.SettingInvoiceView.as_view(),name='settinginvoice'),
    path('settingsalary/',views.SettingSalaryView.as_view(),name='settingsalary'),
    path('settingnotification/',views.SettingNotificationView.as_view(),name='settingnotification'),
    path('changepasswordView/',views.ChangePasswordView.as_view(),name='changepasswordView'),
    path('leavetype/',views.LeaveTypeView.as_view(),name='leavetype'),
    path('employee_search/',search.EmployeeSearchResultsView.as_view(),name='employee_search')
]