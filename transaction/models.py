from django.db import models
from datetime import date

class transaction(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    fromdate = models.DateField(default=date.today)  # Change to DateField with default system date
    todate = models.DateField(default=date.today)    # Change to DateField with default system date
    trdate = models.DateField(default=date.today)    # Change to DateField with default system date
    fromplace = models.CharField(max_length=50)
    toplace = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
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

    class Meta:
        db_table = "tbltransaction_1"
