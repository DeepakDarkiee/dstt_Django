from django import forms
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