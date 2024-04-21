from django.db import models

class Passes(models.Model):  
    name = models.CharField(max_length=100)  
    city = models.CharField(max_length=100)
    passtype_choices = [
        ('Dailypass', 'Dailypass'),
        ('Monthlypass', 'Monthlypass'),
        ('Annualpass', 'Annualpass'),
        ('Differently abled pass', 'Differently Abled pass'),
        ('school pass', 'School pass'),
        ('College pass', 'college pass'),
    ]
    passtype = models.CharField(max_length=100, choices=passtype_choices)
    amount= models.CharField(max_length=100)
        
        
  
    class Meta:  
        db_table = "tblpases_1"
