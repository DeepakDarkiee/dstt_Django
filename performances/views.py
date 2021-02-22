from django.shortcuts import render,redirect
from django.shortcuts import render,HttpResponse
from django.http.response import HttpResponseRedirect
from django.views import generic
from .models import Goal,GoalTracking
from .forms import Goal,GoalTrackingForm, TrainingListForm
from django.contrib import messages
from django.views.generic import View, TemplateView,CreateView,ListView,DeleteView
from .models import Goal,TrainingList,Trainer,TrainingType
from django.views.generic import TemplateView,CreateView,ListView
# from performances.functions import handle_uploaded_file 

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

class GoalTrackingCreateView(View):
    def post(self,request):
        form = GoalTrackingForm(request.POST)  
        if form.is_valid():  
            
            try:  
                form.save() 
                 
                return render(request,'/performances/goaltracking')
            except:  
                pass  
     
        form = TrainingListForm() 
        goal_list = TrainingList.objects.all()

        return render(request,'performances/goal_tracking.html',{'form':form,'objects_list':goal_list,})

# class GoalTrackingCreateView(CreateView):
#     form_class = GoalTrackingForm
#     template_name = "performances/goal_tracking.html" 
#     # fields = ( 'Gole_type', 'GoalTracking_subject', 'GoalTracking_target_achievement',
#     # 'GoalTracking_end_date', 'GoalTracking_discription', 
#     # 'GoalTracking_status', )
    
#     success_url = ('/performances/goaltracking_list')


# class GoalTrackingListView(generic.ListView):
#     model = GoalTracking
#     template_name = "performances/goal_tracking.html"
#     context_object_name = "goaltracking"
#     success_url = ('/performances/goaltracking_list')


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



class GoalTypeRemove(View):
    def get(self,request,id):
            goal_type =Goal.objects.get(id=id)          
            goal_type.delete()
            messages.success(request,"deleted successfully")
            return HttpResponseRedirect('/performances/goaltype_list')


# ---------------------------------  /Goal end ----------------------------------

# -------------------------------------------Training-------------------------------------


def TrainingCreateView(request):
    if request.method == "POST":  
        form = TrainingListForm(request.POST,request.FILES)  
        if form.is_valid():  
            
            try:  
                form.save() 
                 
                return render(request,'performances/trainings.html')
            except:  
                pass  
     
    form = TrainingListForm() 
    training = TrainingList.objects.all()

    return render(request,'performances/trainings.html',{
        'form':form,
        'objects_list':training,
        })

class TrainingRemove(View):
    def get(self,request,id):
            Training_List =TrainingList.objects.get(id=id) 
            # print(TrainingList)         
            Training_List.delete()
            messages.success(request,"deleted successfully")
            return HttpResponseRedirect('/performances/trainings')


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

class TrainerRemove(View):
    def get(self,request,id):
            trainer =Trainer.objects.get(id=id)          
            trainer.delete()
            messages.success(request,"deleted successfully")
            return HttpResponseRedirect('/performances/trainers')  

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