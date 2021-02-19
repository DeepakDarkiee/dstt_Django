from django.db import models

# Create your models here.
#---------------------------------- Goal type  ---------------------------------
Goal_status = (
    ('Active', 'Active'),
    ('Inactive','Inactive')

)


class Goal(models.Model):
    Goal_type = models.CharField(max_length=100)
    # Goal_type = models.ForeignKey(GoalTracking, on_delete=models.CASCADE)
    Goal_discription = models.TextField(max_length=100)
    Goal_status= models.CharField(max_length=100,choices=Goal_status,  null=True, default='Active')
    def __str__(self):
        return self.Goal_type
#---------------------------------- Goal type end ---------------------------------

#---------------------------------- Goal tracking  ---------------------------------
GoalTracking_status = (
    ('Active', 'Active'),
    ('Inactive','Inactive')
)
class GoalTracking(models.Model):
    Gole_type =  models.ForeignKey(Goal, on_delete=models.CASCADE)
    # Gole_type =  models.CharField(max_length=200)
    GoalTracking_subject = models.CharField(max_length=200)
    GoalTracking_target_achievement = models.CharField(max_length=200)
    GoalTracking_start_date =models.DateTimeField(auto_now=True)
    GoalTracking_end_date = models.DateTimeField()
    GoalTracking_discription = models.TextField(max_length=100)
    GoalTracking_status= models.CharField(max_length=100,choices=GoalTracking_status, null=True,
     default='Active')
    def __str__(self):
        return self.GoalTracking_subject
#---------------------------------- Goal tracking end  ---------------------------------
# --------------------------------------------------Training List----------------------------------------------------
TrainingList_status = (
    ('Active', 'Active'),
    ('Inactive','Inactive')
)
class TrainingList(models.Model):
    training_type_type= models.ForeignKey('TrainingType',on_delete=models.CASCADE)
    trainer_name= models.ForeignKey('Trainer',on_delete=models.CASCADE)
    # employee_id= models.ForeignKey('Employee',on_delete=models.CASCADE)
    traininglist_training_cost= models.IntegerField()
    traininglist_duration= models.CharField(max_length=100)
    traininglist_start_date= models.DateTimeField(auto_now_add=True)
    traininglist_end_date= models.DateField()
    traininglist_discription= models.TextField()
    traininglist_status= models.CharField(max_length=100,choices=TrainingList_status,null=True,default='Active')
    traininglist_upload_pdf= models.FileField(upload_to='',null=True, blank="True")
    traininglist_upload_video= models.FileField(upload_to='',null=True, blank="True")
    # traininglist_training_type= models.CharField(max_length=100)
    def __str__(self):
        return self.traininglist_status
    

# --------------------------------------------------/Training List----------------------------------------------------
# --------------------------------------------------Training----------------------------------------------------

trainer_status = (
    ('Active', 'Active'),
    ('Inactive','Inactive')

)
class Trainer(models.Model):
    Trainer_first_name = models.CharField(max_length=100)
    Trainer_last_name = models.CharField(max_length=100)
    Trainer_role = models.CharField(max_length=100)
    Trainer_email = models.EmailField()
    Trainer_phone = models.CharField(max_length=100)
    Trainer_status = models.CharField(choices=trainer_status,max_length=20,default='Active')
    Trainer_desscription = models.TextField(max_length=100)
    def __str__(self):
        return self.Trainer_first_name

# --------------------------------------------------Training----------------------------------------------------

# --------------------------------------------------Training Type----------------------------------------------------
TrainingType_status = (
    ('Active', 'Active'),
    ('Inactive','Inactive')
)
class TrainingType(models.Model):
    training_type_type = models.CharField(max_length=100)
    trainingtype_description = models.TextField(max_length=100)
    trainingtype_status = models.CharField(max_length=100,choices=TrainingType_status, null=True,
     default='Active')
    def __str__(self):
        return self.training_type_type

# --------------------------------------------------Training Type----------------------------------------------------

    
