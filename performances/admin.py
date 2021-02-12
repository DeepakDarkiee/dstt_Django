from django.contrib import admin
from .models import Goal
# Register your models here.


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    class Meta:
        model = Goal
        fields = '__all__'
