from django import forms
from .models import Goal

class GoleForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = "__all__"