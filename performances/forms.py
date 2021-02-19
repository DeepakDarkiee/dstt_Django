from django import forms
from .models import Goal,GoalTracking,TrainingList,TrainingType,Trainer

# ----------------------------------------Goal--------------------------------------------------
class GoleForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = "__all__"
# ----------------------------------------Goal end--------------------------------------------------
# ----------------------------------------Goal tracking-------------------------------------------------------
class GoalTrackingForm(forms.ModelForm):
    class Meta:
        model = GoalTracking
        fields = "__all__"
# ----------------------------------------Goal tracking end-------------------------------------------------------
# ----------------------------------------Training List -------------------------------------------------------
class TrainingListForm(forms.ModelForm):
    class Meta:
        model = TrainingList
        fields = "__all__"
# ----------------------------------------Training List end -------------------------------------------------------
# ----------------------------------------Trainer--------------------------------------------------
class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = "__all__"
# ----------------------------------------/Trainer end--------------------------------------------------
# ----------------------------------------Training Type -------------------------------------------------------
class TrainingTypeForm(forms.ModelForm):
    class Meta:
        model = TrainingType
        fields = "__all__"
        
# ----------------------------------------Training Type end -------------------------------------------------------
