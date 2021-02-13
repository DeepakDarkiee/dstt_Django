from django import forms
from .models import Goal,GoalTracking

class GoleForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = "__all__"

class GoalTrackingForm(forms.ModelForm):
    class Meta:
        model = GoalTracking
        fields = "__all__"