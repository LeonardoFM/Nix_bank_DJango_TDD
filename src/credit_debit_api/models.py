from django.db import models
import datetime

class VirtualAccount(models.Model):
    name = models.CharField(max_length=50)
    agency = models.CharField(max_length=5)
    current_account = models.CharField(max_length=9)

    def __str__(self):        
        return self.name
    
    @property
    def has_agency(self):
        return self.agency != '000-0'

class Transaction(models.Model):
    date = models.DateField(auto_now=datetime.date.today())
    description = models.CharField(max_length=20)
    balance = models.IntegerField()
    debit =  models.IntegerField(null=True,blank=True)
    credit =  models.IntegerField(null=True,blank=True)
    status = models.CharField(max_length=1)
    account = models.ForeignKey(VirtualAccount, on_delete=models.CASCADE)

    def __str__(self):        
        return self.description

    @property
    def is_in_debit(self):
        return self.status == 'D'
    
    @property
    def is_in_credit(self):
        return self.status == 'C'

    