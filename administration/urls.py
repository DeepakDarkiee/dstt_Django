from django.urls import path
from . import views

urlpatterns = [
    path('index/',views.IndexView.as_view(),name='index' ),
    path('clients/',views.ClientsView.as_view(),name='clients' ),
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
]