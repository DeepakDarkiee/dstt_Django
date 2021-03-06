from django import forms
from .models import Goal,GoalTracking,TrainingList,TrainingType,Trainer,Termination

# ----------------------------------------Goal--------------------------------------------------
class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        
        fields = "__all__"
        exclude = ('Goal_status',)
# ----------------------------------------Goal end--------------------------------------------------
# ----------------------------------------Goal tracking-------------------------------------------------------
class GoalTrackingForm(forms.ModelForm):
    class Meta:
        model = GoalTracking
        widgets = {
            'End_Date':forms.DateInput(attrs={'type':'date'})
        }
        fields = "__all__"
        exclude = ('Status',)
# ----------------------------------------Goal tracking end-------------------------------------------------------
# ----------------------------------------Training List -------------------------------------------------------
class TrainingListForm(forms.ModelForm):
    class Meta:
        model = TrainingList
        widgets = {
            'End_Date' : forms.DateInput(attrs={'type':'date'})
        }
        fields = "__all__"
        exclude =('Status',)
# ----------------------------------------Training List end -------------------------------------------------------
# ----------------------------------------Trainer--------------------------------------------------
class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = "__all__"
        exclude =('Trainer_status',)
# ----------------------------------------/Trainer end--------------------------------------------------
# ----------------------------------------Training Type -------------------------------------------------------
class TrainingTypeForm(forms.ModelForm):
    class Meta:
        model = TrainingType
        fields = "__all__"
        exclude = ('trainingtype_status',)
        
# ----------------------------------------Training Type end -------------------------------------------------------
# ---------------------------------------- Termination -------------------------------------------------------

class TerminationForm(forms.ModelForm):
    class Meta:
        model = Termination
        widgets = {
            'Termination_Date' : forms.DateInput(attrs={'type':'date'}),
            'Notice_Date' : forms.DateInput(attrs={'type':'date'})
        }
        fields = "__all__"

# ---------------------------------------- /Termination -------------------------------------------------------