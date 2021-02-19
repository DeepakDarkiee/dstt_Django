from django import forms
<<<<<<< HEAD
from .models import TrainingType,Trainers

# ---------------------------------------- Form Trainers ------------------------------------------------------
class TrainersForm(forms.ModelForm):
    class meta:
        model = Trainers
        fields = "__all__"
# ---------------------------------------- /Form Trainers ------------------------------------------------------

# ---------------------------------------- Form Training Type ------------------------------------------------------
class TrainingTypeForm(forms.ModelForm):
    class meta:
        model = TrainingType
        fields = "__all__"
# ---------------------------------------- /Form Training Type ------------------------------------------------------
=======
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
>>>>>>> 0a77c39c2a5b991ee4bc0b2a32d68e252dfdd948
