from django.shortcuts import render
from django.shortcuts import render,HttpResponse
from django.http.response import HttpResponseRedirect
from django.views import generic
from .models import Goal,GoalTracking
from .forms import Goal,GoalTracking
from django.contrib import messages
from django.views.generic import View, TemplateView,CreateView,ListView,DeleteView
from .models import Goal,TrainingList,Trainer,TrainingType
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

# ---------------------------------  Goal tracking----------------------------------
class GoalTrackingCreateView(generic.CreateView):
    model = GoalTracking
    template_name = "performances/goal_tracking.html" 
    fields = ( 'Gole_type', 'GoalTracking_subject', 'GoalTracking_target_achievement',
    'GoalTracking_start_date','GoalTracking_end_date', 'GoalTracking_discription', 
    'GoalTracking_status', )
    # context_object_name = "goal_type"
    success_url = ('/performances/goaltracking_list')

class GoalTrackingListView(generic.ListView):
    model = GoalTracking
    template_name = "performances/goal_tracking.html"
    context_object_name = "goaltracking"
    success_url = ('/performances/goaltracking_list')

# class GoalTrackingRemove(View):
#     def get(self,request,id):
#             goaltracking=GoalTracking.objects.get(id=id)          
#             goaltracking.delete()
#             messages.success(request,"deleted successfully")
#             return HttpResponseRedirect('/performances/goaltracking_list')

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
    success_url = ('/performances/goaltype')
# ---------------------------------  /Goal ----------------------------------

# -------------------------------------------Training-------------------------------------
class trainingCreateView(generic.CreateView):
    model=TrainingList
    fields=('training_type_type', 'trainer_name','traininglist_training_cost',
     'traininglist_duration', 'traininglist_end_date',
      'traininglist_discription', 'traininglist_status', 'traininglist_upload_pdf', 
      'traininglist_upload_video',)
    template_name = "performances/trainings.html"
    
# -------------------------------------------/Training-------------------------------------
# -------------------------------------------Trainer-------------------------------------
class TrainersCreateView(generic.CreateView):
    model = Trainer
    fields = ('Trainer_first_name', 'Trainer_last_name', 'Trainer_role', 'Trainer_email', 'Trainer_phone', 'Trainer_status', 'Trainer_desscription')
    template_name = "performances/trainers.html"
    success_url = ('/performances/trainer_list')

class TrainersListView(generic.ListView):
    model = Trainer
    template_name = "performances/trainers.html"
    context_object_name = "trainer_list"
    success_url = ('/performances/trainers')

class TrainersRemove(View):
    def get(self,request,id):
            training_type =TrainingType.objects.get(id=id)          
            training_type.delete()
            messages.success(request,"deleted successfully")
            return HttpResponseRedirect('/performances/trainer_list')    
# -------------------------------------------/Trainer-------------------------------------
# -------------------------------------------Training Type ------------------------------------------
class TrainingTypeCreateView(generic.CreateView):
    model= TrainingType
    fields = ('training_type_type', 'trainingtype_description', 'trainingtype_status')
    template_name = "performances/trainings_type.html"
    success_url = ('/performances/training_type_list')

class TrainingTypeListView(generic.ListView):
    model = TrainingType
    template_name = "performances/trainings_type.html"
    context_object_name = "training_type_list"
    success_url = ('/performances/training_type')

class TrainingTypeRemove(View):
    def get(self,request,id):
            training_type =TrainingType.objects.get(id=id)          
            training_type.delete()
            messages.success(request,"deleted successfully")
            return HttpResponseRedirect('/performances/training_type_list')
# ------------------------------------------- /Training Type ------------------------------------------
class promotionView(TemplateView):
    template_name = "performances/promotion.html"

class resignationView(TemplateView):
    template_name = "performances/resignation.html"

class terminationView(TemplateView):
    template_name = "performances/termination.html"