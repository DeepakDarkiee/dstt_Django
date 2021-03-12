from django.db import models


cilent_status = (
    ('Active', 'Active'),
    ('Inactive','Inactive')

)

asset_status = (
    ('new','new'),
    ('pending','pending'),
    ('damaged','damaged'),
    ('deployed','deployed'),
    ('approved','approved')
)



#--------------------------------------------------------Client-----------------------------------------------------------------------
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
#--------------------------------------------------------/Client-----------------------------------------------------------------------

#--------------------------------------------------------Assets-----------------------------------------------------------------------
class Asset(models.Model):
    asset_name = models.CharField(max_length=100)
    asset_id = models.CharField(max_length=100)
    asset_purcahse_date  =models.CharField(max_length=100)
    asset_purcahse_from = models.CharField(max_length=100)
    asset_manufacture = models.CharField(max_length=100)
    asset_model = models.CharField(max_length=100)
    asset_serial_number = models.CharField(max_length=100)
    asset_supplier = models.CharField(max_length=100)
    asset_conditiion = models.CharField(max_length=50)
    asset_warrenty = models.CharField(max_length=100)
    asset_amount = models.IntegerField()
    asset_user = models.CharField(max_length=100)
    asset_description = models.TextField()
    asset_status = models.CharField(max_length=20,choices=asset_status,default='new')
#--------------------------------------------------------/Assets-----------------------------------------------------------------------

#--------------------------------------------------------Leads-----------------------------------------------------------------------
class Lead(models.Model):
    lead_name = models.CharField(max_length=100)
    lead_email = models.EmailField()
    lead_phone = models.CharField(max_length=100)
    lead_project = models.CharField(max_length=100)
    lead_assign_staff = models.CharField(max_length=100)
    lead_created = models.CharField(max_length=100)
#--------------------------------------------------------/Leads-----------------------------------------------------------------------



