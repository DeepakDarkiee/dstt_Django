from django.contrib import admin
from .models import Client,Asset,Lead

# Register your models here.
# -------------------------------------Client---------------------------------------------------
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    class Meta:
        model = Client
        fields = '__all__'
# -------------------------------------/Client---------------------------------------------------

# -------------------------------------Assets---------------------------------------------------
@admin.register(Asset)
class ClientAdmin(admin.ModelAdmin):
    class Meta:
        model = Asset
        fields = '__all__'
# -------------------------------------/Assets---------------------------------------------------

# -------------------------------------Leads---------------------------------------------------
@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    class Meta:
        model = Lead
        fields = '__all__'
# -------------------------------------/Leads---------------------------------------------------