from django.db import models

# Create your models here.
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
