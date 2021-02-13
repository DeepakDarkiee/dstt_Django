from django.db import models

# Create your models here.
#---------------------------------- Goal type  ---------------------------------
Goal_status = (
    ('Active', 'Active'),
    ('Inactive','Inactive')

)
class Goal(models.Model):
    Goal_type = models.CharField(max_length=100)
    Goal_discription = models.TextField(max_length=100)
    Goal_status= models.CharField(max_length=100,choices=Goal_status, default = 'Active')
    def __str__(self):
        return self.Goal_type
#---------------------------------- Goal type end ---------------------------------

#---------------------------------- Goal tracking  ---------------------------------
GoalTracking_status = (
    ('Active', 'Active'),
    ('Inactive','Inactive')
)
class GoalTracking(models.Model):
    Gole_type =  models.CharField(max_length=200)
    GoalTracking_subject = models.CharField(max_length=200)
    GoalTracking_target_achievement = models.CharField(max_length=200)
    GoalTracking_start_date = models.CharField(max_length=200)
    GoalTracking_end_date = models.CharField(max_length=200)
    GoalTracking_discription = models.TextField(max_length=100)
    GoalTracking_status= models.CharField(max_length=100,choices=GoalTracking_status, default = 'Active')
    def __str__(self):
        return self.GoalTracking_subject
#---------------------------------- Goal tracking end  ---------------------------------
