from django.shortcuts import render
from django.shortcuts import render,HttpResponse
from django.http.response import HttpResponseRedirect
from django.views import generic
from .models import Goal,GoalTracking
from django.contrib import messages
from django.views.generic import View, TemplateView,CreateView,ListView,DeleteView

# Create your views here.
class performanceindicatorView(TemplateView):
    template_name = "performances/performance_indicator.html"

class performanceView(TemplateView):
    template_name = "performances/performance.html"

class performanceappraisalView(TemplateView):
    template_name = "performances/performance_appraisal.html"

class performanceIndicatorView(TemplateView):
    template_name = "performances/performance_indicator.html"

# ---------------------------------  Goal tracking----------------------------------
class GoalTrackingCreateView(generic.CreateView):
    model = GoalTracking
    fields = ('Gole_type', 'GoalTracking_subject', 'GoalTracking_target_achievement','GoalTracking_start_date', 'GoalTracking_end_date', 'GoalTracking_discription', 'GoalTracking_status' )
    template_name = "performances/goal_tracking.html" 
    success_url = ('/performances/goaltracking_list')

class GoalTrackingListView(generic.ListView):
    model = GoalTracking
    template_name = "performances/goal_tracking.html"
    context_object_name = "goaltracking"
    success_url = ('/performances/goaltracking_list')

class GoalTrackingRemove(View):
    def get(self,request,id):
            goaltracking=GoalTracking.objects.get(id=id)          
            goaltracking.delete()
            messages.success(request,"deleted successfully")
            return HttpResponseRedirect('/performances/goaltracking_list')

        # except GoalTracking.DoesNotExist:
            # messages.error(request,"Role already Deleted or Not Created")

# ---------------------------------  Goal tracking end ---------------------------------------
# ---------------------------------  Goal ----------------------------------
class GoalTypeCreateView(generic.CreateView):
    model = Goal
    fields = ('Goal_type', 'Goal_discription', 'Goal_status')
    template_name = "performances/goal_type.html"
    success_url = ('/performances/goaltype_list')

class GoalTypeListView(generic.ListView):
    model = Goal
    template_name = "performances/goal_type.html"
    context_object_name = "goletype"
    success_url = ('/performances/goaltype_list')

class GoalTypeRemove(generic.DeleteView):
    model = Goal
    template_name = "performances/goal_type.html"
    # context_object_name = "goletype_delete"
    success_url =  ('/performances/goaltype_list')


# class GoalTypeRemove(View):
#     def get(self,request,id):
#             goal=Goal.objects.get(id=id)          
#             goal.delete()
#             messages.success(request,"deleted successfully")
#             return HttpResponseRedirect('/performances/goaltype_list')

# ---------------------------------  /Goal end ----------------------------------
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


