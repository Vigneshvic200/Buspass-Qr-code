from django.db import models

# Create your models here.
class passenger(models.Model):  
    name = models.CharField(max_length=100)  
    city = models.CharField(max_length=100)  
    contact = models.CharField(max_length=15) 
   
    class Meta:  
        db_table = "tblpassenger"