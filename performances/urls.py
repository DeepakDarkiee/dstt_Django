from django.urls import path
from . import views

urlpatterns = [
    path('performanceindicator/',views.performanceindicatorView.as_view(),name='performanceindicator'),
    path('performance/',views.performanceView.as_view(),name='performance'),
    path('performanceappraisal/',views.performanceappraisalView.as_view(),name='performanceappraisal'),
    path('performanceindicator/',views.performanceIndicatorView.as_view(),name='performanceindicator'),
    path('goaltracking/',views.goalTrackingView.as_view(),name='goaltracking'),
    path('goaltype/',views.goalTypeView.as_view(),name='goaltype'),
    path('trainings/',views.trainingsView.as_view(),name='trainings'),
    path('trainers/',views.trainersView.as_view(),name='trainers'),
    path('trainingstype/',views.trainingsTypeView.as_view(),name='trainingstype'),
    path('promotion/',views.promotionView.as_view(),name='promotion'),
    path('resignation/',views.resignationView.as_view(),name='resignation'),
    path('termination/',views.terminationView.as_view(),name='termination'),
   
]