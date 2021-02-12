
from django.db import models


cilent_status = (
    ('Active', 'Active'),
    ('Inactive','Inactive')

)

# Create your models here.
class Client(models.Model):
    client_first_name  = models.CharField(max_length=100)
    client_last_name = models.CharField(max_length=100)
    client_username = models.CharField(max_length=100, unique=True)
    client_email = models.EmailField(max_length=100)
    client_id = models.CharField(max_length=100)
    client_address = models.CharField(max_length=100)
    client_phone=models.CharField(max_length=100)    
    client_status = models.CharField(choices=cilent_status,max_length=20,default='Active')
    def __str__(self):
        return self.client_first_name
