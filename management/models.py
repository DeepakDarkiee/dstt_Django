from django.db import models

# Create your models here.
#---------------------------------- Policy  ---------------------------------

class Policy(models.Model):
    Policy_name = models.CharField(max_length=200)
    Policy_Description = models.TextField(max_length=200)
    Policy_Department = models.CharField(max_length=200)
    Policy_Upload_Policy = models.FileField(upload_to='',null=True, blank="True")
    def __str__(self):
        return self.Policy_name
#---------------------------------- Policy end  ---------------------------------