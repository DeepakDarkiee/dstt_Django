from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.IndexView.as_view(),name='index' ),
    path('clients/',views.CreateClientsView.as_view(),name='clients' ),
    path('clients_list/',views.CreateClientsListView.as_view(),name='clients_list' ),
    path('clients_grid/',views.CreateClientsGridView.as_view(),name='clients_grid' ),
    path('leads/',views.LeadsView.as_view(),name='leads' ),
    path('projects/',views.projectsView.as_view(),name='projects' ),
    path('taskboard/',views.taskboardView.as_view(),name='taskboard' ),
    path('assets/',views.assetsView.as_view(),name='assets' ),
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