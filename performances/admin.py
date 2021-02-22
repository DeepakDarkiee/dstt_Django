from django.contrib import admin
from .models import Goal,Trainer,TrainingType,TrainingList
# Register your models here.


# -------------------------------------------Goal--------------------------------------------------------
@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    class Meta:
        model = Goal
        fields = '__all__'
# -------------------------------------------/Goal--------------------------------------------------------
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
