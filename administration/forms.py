from django import forms
<<<<<<< HEAD
from .models import Lead
class LeadForm(forms.ModelForm):
    class meta:
        model = Lead
        fields = "__all__"
=======
from .models import Client,Asset,Lead

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
        fields = "__all__"

# --------------------------------------/Assets----------------------------------------------------

# --------------------------------------Lead----------------------------------------------------
class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = "__all__"

# --------------------------------------/Lead----------------------------------------------------
>>>>>>> 0a77c39c2a5b991ee4bc0b2a32d68e252dfdd948
