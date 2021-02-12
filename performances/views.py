from django.shortcuts import render
from django.shortcuts import render,HttpResponse
from django.views import generic
from .models import Goal

from django.views.generic import TemplateView,CreateView,ListView

# Create your views here.
class performanceindicatorView(TemplateView):
    template_name = "performances/performance_indicator.html"

class performanceView(TemplateView):
    template_name = "performances/performance.html"

class performanceappraisalView(TemplateView):
    template_name = "performances/performance_appraisal.html"

class performanceIndicatorView(TemplateView):
    template_name = "performances/performance_indicator.html"

class goalTrackingView(TemplateView):
    template_name = "performances/goal_tracking.html"
# ---------------------------------  Goal ----------------------------------
class goalTypeCreateView(generic.CreateView):
    model = Goal
    fields = ('Goal_type', 'Goal_discription', 'Goal_status')
    template_name = "performances/goal_type.html"
    success_url = ('/performances/goaltype')
# ---------------------------------  /Goal ----------------------------------
class trainingsView(TemplateView):
    template_name = "performances/trainings.html"

class trainersView(TemplateView):
    template_name = "performances/trainers.html"

class trainingsTypeView(TemplateView):
    template_name = "performances/trainings_type.html"

class promotionView(TemplateView):
    template_name = "performances/promotion.html"

class resignationView(TemplateView):
    template_name = "performances/resignation.html"

class terminationView(TemplateView):
    template_name = "performances/termination.html"


