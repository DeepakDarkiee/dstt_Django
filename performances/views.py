from django.shortcuts import render,redirect,get_object_or_404

from django.shortcuts import render,HttpResponse
from django.http.response import HttpResponseRedirect
from django.views import generic
from .models import Goal,GoalTracking
from .forms import GoalForm,GoalTrackingForm, TrainingListForm
from django.contrib import messages
from django.views.generic import View, TemplateView,CreateView,ListView,DeleteView,UpdateView
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


def GoalTrackingCreateView(request):
    if request.method == "POST":  
        form = GoalTrackingForm(request.POST,request.FILES)  
        if form.is_valid():  
            
            try:  
                form.save() 
                 
                return render(request,'performances/goal_tracking.html')
            except:  
                pass  
     
    form = GoalTrackingForm() 
    goaltracking = GoalTracking.objects.all()

    return render(request,'performances/goal_tracking.html',{
        'form':form,
        'objects_list':goaltracking,
        })

# class GoalTrackingManage(generic.UpdateView):
#     form_class = GoalTrackingForm
#     template_name = 'performances/goal_tracking.html'
#     success_url = ('performances/goaltracking')


def GoalTrackingEdit(request,id):
    goal_trackings = GoalTracking.objects.get(id=id)
    goal_type = Goal.objects.all()
    print(goal_type)
    return render(request,"performances/goal_tracking.html",{'goal_trackings':goal_trackings,'goal_type':goal_type})


def GoalTrackingManage(request,id):
    goal_trackings = GoalTracking.objects.get(id=id) 
    print(goal_trackings)
    goaltypes =Goal.objects.all()
    if request.method == "POST":     
        goal_trackings.Goal_type = Goal.objects.get(Goal_type=request.POST.get('Goal_type',''))
        goal_trackings.Subject = request.POST.get('Subject','')
        goal_trackings.Target_Achievement = request.POST.get('Target_Achievement','')
        goal_trackings.Start_Date = request.POST.get('Start_Date','')
        goal_trackings.End_Date = request.POST.get('End_Date','')
        goal_trackings.Discription = request.POST.get('Discription','')
        goal_trackings.Status = request.POST.get('Status','')
        print(goal_trackings)
        goal_trackings.save()
        messages.success(request,"Update successfully")
        return render(request,'performances/goal_tracking.html',{'goaltypes':goaltypes,'goal_trackings':goal_trackings})

# def GoalTrackingManage(request, id): 
#     instance = get_object_or_404(GoalTracking, id=id)
#     form = GoalTrackingForm(request.POST or None, instance=instance)
#     if form.is_valid():
#         form.save()
#         return redirect('/performances/goaltracking')
#     return render(request, '/performances/goal_tracking.html', {'form': form}) 


class GoalTrackingRemove(View):
    def get(self,request,id):
            goal_tracking =GoalTracking.objects.get(id=id)          
            goal_tracking.delete()
            messages.success(request,"deleted successfully")
            return HttpResponseRedirect('/performances/goaltracking')



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

# class GoalTypeManage(View):
#     form_class = GoalForm
#     def get(self,request,id):
#             goal_type =Goal.objects.get(id=id)          
#             goal_type.update()
#             messages.success(request,"update successfully")
#             return HttpResponseRedirect('/performances/goaltype_list')


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