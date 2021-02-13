from django.contrib import admin
from .models import Policy
# Register your models here.

@admin.register(Policy)
class PolicyAdmin(admin.ModelAdmin):
    class Meta:
        model = Policy
        fields = '__all__'
