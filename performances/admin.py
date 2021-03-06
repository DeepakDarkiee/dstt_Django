from django.contrib import admin
from .models import Goal,GoalTracking,Trainer,TrainingType,TrainingList,Termination
# Register your models here.


# -------------------------------------------Goal--------------------------------------------------------
@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    class Meta:
        model = Goal
        fields = '__all__'
# -------------------------------------------/Goal--------------------------------------------------------
# -------------------------------------------Goal tracking--------------------------------------------------------
@admin.register(GoalTracking)
class GoalTrackingAdmin(admin.ModelAdmin):
    class Meta:
        model = GoalTracking
        fields = '__all__'
# -------------------------------------------/Goal tracking----------------------------------------------------------------------------------------
# -------------------------------------------Training List--------------------------------------------------------
@admin.register(TrainingList)
class TrainingList(admin.ModelAdmin):
    class Meta:
        model = TrainingList
        fields = '__all__'
# -------------------------------------------/Training List--------------------------------------------------------
# -------------------------------------------Trainer--------------------------------------------------------
@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    class Meta:
        model = Trainer
        fields = '__all__'
# -------------------------------------------/Trainer--------------------------------------------------------
# -------------------------------------------Training  Type--------------------------------------------------------
@admin.register(TrainingType)
class TrainingTypeAdmin(admin.ModelAdmin):
    class Meta:
        model = TrainingType
        fields = '__all__'
# -------------------------------------------/Training Type--------------------------------------------------------
# -------------------------------------------Termination--------------------------------------------------------
@admin.register(Termination)
class TerminationAdmin(admin.ModelAdmin):
    class Meta:
        model = Termination
        fields = '__all__'
# -------------------------------------------/Termination--------------------------------------------------------
