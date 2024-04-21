from django.db import models
import uuid

from django.db import models

class transaction(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=100)  
    city = models.CharField(max_length=100)
    fromdate = models.DateField()
    todate = models.DateField()
    trdate = models.DateField()
    fromplace = models.CharField(max_length=50)  # Fix the typo here
    toplace = models.CharField(max_length=50)    # Fix the typo here
    address = models.CharField(max_length=50)    # Fix the typo here
    amount = models.CharField(max_length=100)  
    contact = models.CharField(max_length=15)
    passtype_choices = [
        ('Dailypass', 'Dailypass'),
        ('Monthlypass', 'Monthlypass'),
        ('Annualpass', 'Annualpass'),
        ('Differently abled pass', 'Differently Abled pass'),
        ('school pass', 'School pass'),
        ('College pass', 'college pass'),
        # Add more options as needed
    ]
    passtype = models.CharField(max_length=100, choices=passtype_choices)

    def __str__(self):
            return str(self.uuid)
   
    

