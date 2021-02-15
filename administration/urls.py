from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.IndexView.as_view(),name='index' ),
# ------------------------------client---------------------------------------------------------------------------
    path('clients/',views.CreateClientsView.as_view(),name='clients' ),
    path('clients_list/',views.CreateClientsListView.as_view(),name='clients_list' ),
    path('clients_grid/',views.CreateClientsGridView.as_view(),name='clients_grid' ),
    path('clients_remove/<int:id>',views.ClientRemove.as_view(),name='clients_remove' ),
    path('clients_remove_grid/<int:id>',views.ClientRemoveGrid.as_view(),name='clients_remove_grid' ),
# ------------------------------client--------------------------------------------------------------------------

# ------------------------------Lead---------------------------------------------------------------------------
    path('leads/',views.CreateLeadView.as_view(),name='leads' ),
    path('leads_list/',views.CreateLeadListView.as_view(),name='leads_list' ),
# ------------------------------/Lead--------------------------------------------------------------------------

    path('projects/',views.projectsView.as_view(),name='projects' ),
    path('taskboard/',views.taskboardView.as_view(),name='taskboard' ),

# -----------------------------------Assets-----------------------------------------------------------------------
    path('assets/',views.AssetCreateView.as_view(),name='assets' ),
    path('asset_list/',views.AssetListView.as_view(),name='asset_list' ),
    # path('asset_remove/<int:id>',views.AssetRemove.as_view(),name='asset_remove' ),
    path('asset_remove/<int:id>',views.AssetRemove.as_view(),name='asset_remove'),
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
]