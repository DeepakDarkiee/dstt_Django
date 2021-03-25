from django import forms
from .models import Client,Asset,Lead,Project
from employee.models import AddLeaveType

# --------------------------------------Client----------------------------------------------------
class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = "__all__"
# --------------------------------------/Client----------------------------------------------------

# --------------------------------------Assets----------------------------------------------------
class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        widgets = {
            'lead_created':forms.DateInput(attrs={'type':'date'})
        }
        fields = "__all__"  
# --------------------------------------/Assets----------------------------------------------------

# --------------------------------------Lead----------------------------------------------------
class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = "__all__"

# --------------------------------------/Lead----------------------------------------------------

#---------------------------------------Project---------------------------------------------------
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = "__all__"
    
#-----------------------------------------AddLeaveType-------------------------------------------------
class AddLeaveTypeForm(forms.ModelForm):
    class Meta:
        model = AddLeaveType
        fields = "__all__"