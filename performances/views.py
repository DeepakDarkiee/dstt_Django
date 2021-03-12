from django.shortcuts import render,redirect
from django.shortcuts import render,HttpResponse,get_object_or_404
from django.http.response import HttpResponseRedirect
from django.views import generic
from .models import Goal,GoalTracking
from .forms import GoalForm, TrainingListForm,TrainerForm,TrainingTypeForm,GoalTrackingForm,TerminationForm
from django.contrib import messages
from django.views.generic import View, TemplateView,CreateView,ListView,DeleteView
from .models import Goal,TrainingList,Trainer,TrainingType,Termination
from django.views.generic import TemplateView,CreateView,ListView,UpdateView

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
                return HttpResponseRedirect('/performances/goaltracking/')
            except:  
                pass  
    def get(self,request):
        form = GoalTrackingForm() 
        goaltracking = GoalTracking.objects.all()

        return render(request,'performances/goal_tracking.html',{
            'form':form,
            'objects_list':goaltracking,
            })
# def GoalTrackingCreateView(request):
#     if request.method == "POST":  
#         form = GoalTrackingForm(request.POST,request.FILES)  
#         if form.is_valid():  
            
#             try:  
#                 form.save() 
                 
#                 return render(request,'performances/goal_tracking.html')
#             except:  
#                 pass  
     
#     form = GoalTrackingForm() 
#     goaltracking = GoalTracking.objects.all()

#     return render(request,'performances/goal_tracking.html',{
#         'form':form,
#         'objects_list':goaltracking,
#         })

class GoalTrackingManage(generic.UpdateView):
    model = GoalTracking
    context_object_name = "goal_tracking"
    fields = ('Gole_Type','Subject','Target_Achievement','Start_Date','End_Date','Discription','Status')
    template_name = "performances/goal_tracking_manage.html"
    success_url = ("/performances/goaltracking/")

class GoalTrackingRemove(View):
    def get(self,request,id):
            goal_tracking =GoalTracking.objects.get(id=id)          
            goal_tracking.delete()
            messages.success(request,"deleted successfully")
            return HttpResponseRedirect('/performances/goaltracking')


# ---------------------------------  Goal tracking end ---------------------------------------

# ---------------------------------  Goal ----------------------------------
class GoalTypeCreateView(View):
    def post(self,request):  
            form = GoalForm(request.POST,request.FILES)  
            if form.is_valid():  
                try:  
                    form.save()  
                    return HttpResponseRedirect('/performances/goaltype/')
                except:  
                    pass  
    def get(self,request):
            form = GoalForm() 
            goal = Goal.objects.all()

            return render(request,'performances/goal_type.html',{
                'form':form,
                'objects_list':goal,
                })

class GoalTypeManage(UpdateView):
    model = Goal
    context_object_name = "goal_type"
    fields = ('Goal_type','Goal_discription','Goal_status')
    template_name = "performances/goal_type_manage.html"
    success_url = ("/performances/goaltype/")


class GoalTypeRemove(View):
    def get(self,request,id):
            goal_type =Goal.objects.get(id=id)          
            goal_type.delete()
            messages.success(request,"deleted successfully")
            return HttpResponseRedirect('/performances/goaltype')
       

                       #-----Generic view----------------

# class GoalTypeCreateView(generic.CreateView):
#     model = Goal
#     fields = ('Goal_type', 'Goal_discription')
#     template_name = "performances/goal_type.html"
#     success_url = ('/performances/goaltype_list')

# class GoalTypeListView(generic.ListView):
#     model = Goal
#     template_name = "performances/goal_type.html"
#     context_object_name = "goaltype"
#     success_url = ('/performances/goaltype_list')





# ---------------------------------  /Goal end ----------------------------------------
# -------------------------------------------Training-------------------------------------

class TrainingCreateView(View):
    def post(self,request):  
        form = TrainingListForm(request.POST,request.FILES)  
        if form.is_valid():  
            try:  
                form.save()  
                return HttpResponseRedirect('/performances/trainings/')
            except:  
                pass  
    def get(self,request):
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
class TrainersCreateView(View):
    def post(self,request):  
        form = TrainerForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return HttpResponseRedirect('/performances/trainers/')
            except:  
                pass  
    def get(self,request):
        form = TrainerForm() 
        trainer = Trainer.objects.all()

        return render(request,'performances/trainers.html',{
            'form':form,
            'objects_list':trainer,
            })

class TrainerManage(generic.UpdateView):
    model = Trainer
    context_object_name = "trainer"
    fields = ('Trainer_first_name','Trainer_last_name','Trainer_role','Trainer_email','Trainer_phone',
    'Trainer_status','Trainer_desscription')
    template_name = "performances/trainer_manage.html"
    success_url = ("/performances/trainers/")

class TrainerRemove(View):
    def get(self,request,id):
            trainer =Trainer.objects.get(id=id)          
            trainer.delete()
            messages.success(request,"deleted successfully")
            return HttpResponseRedirect('/performances/trainers')

    
# class TrainersCreateView(generic.CreateView):
#     model = Trainer
#     fields = ('Trainer_first_name', 'Trainer_last_name', 'Trainer_role', 'Trainer_email', 'Trainer_phone',  'Trainer_desscription')
#     template_name = "performances/trainers.html"
#     success_url = ('/performances/trainer_list')

# class TrainersListView(generic.ListView):
#     model = Trainer
#     template_name = "performances/trainers.html"
#     context_object_name = "trainer_list"
#     success_url = ('/performances/trainers')

# -------------------------------------------/Trainer-------------------------------------
# -------------------------------------------Training Type ------------------------------------------
class TrainingTypeCreateView(View):
    def post(self,request):  
        form = TrainingTypeForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return HttpResponseRedirect('/performances/training_type/')
            except:  
                pass  
    def get(self,request):
        form = TrainingTypeForm() 
        training_type = TrainingType.objects.all()

        return render(request,'performances/trainings_type.html',{
            'form':form,
            'objects_list':training_type,
            })

class TrainingTypeManage(generic.UpdateView):
    model = TrainingType
    context_object_name = "training_type"
    fields = ('training_type_type','trainingtype_description','trainingtype_status')
    template_name = "performances/trainings_type_manage.html"
    success_url = ("/performances/training_type/")

class TrainingTypeRemove(View):
    def get(self,request,id):
            training_type =TrainingType.objects.get(id=id)          
            training_type.delete()
            messages.success(request,"deleted successfully")
            return HttpResponseRedirect('/performances/training_type')


# class TrainingTypeCreateView(generic.CreateView):
#     model= TrainingType
#     fields = ('training_type_type', 'trainingtype_description')
#     template_name = "performances/trainings_type.html"
#     success_url = ('/performances/training_type_list')

# class TrainingTypeListView(generic.ListView):
#     model = TrainingType
#     template_name = "performances/trainings_type.html"
#     context_object_name = "training_type_list"
#     success_url = ('/performances/training_type')

# ------------------------------------------- /Training Type ------------------------------------------
class promotionView(TemplateView):
    template_name = "performances/promotion.html"

class resignationView(TemplateView):
    template_name = "performances/resignation.html"

# ------------------------------------------- Termination ------------------------------------------

class TerminationCreate(View):
    def post(self,request):  
        form = TerminationForm(request.POST or None)  
        if form.is_valid():  
            try:  
                # Notice_Date = form.cleaned_data['Notice_Date']
                form.save()  
                return HttpResponseRedirect('/performances/termination/')
            except:  
                pass  
    def get(self,request):
        form = TerminationForm() 
        termination = Termination.objects.all()

        return render(request,'performances/termination.html',{
            'form':form,
            'objects_list':termination,
            })

class TerminationRemove(View):
    def get(self,request,id):
        termination= Termination.objects.get(id=id)
        termination.delete()
        messages.success(request,"deleted successfully")
        return HttpResponseRedirect('/performances/termination')
        

# ------------------------------------------- /Termination ------------------------------------------