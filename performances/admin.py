from django.contrib import admin
from .models import Goal,GoalTracking
# Register your models here.


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    class Meta:
        model = Goal
        fields = '__all__'

@admin.register(GoalTracking)
class GoalGoalTrackingAdmin(admin.ModelAdmin):
    class Meta:
        model = GoalTracking
        fields = '__all__'



