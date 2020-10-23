from django.db import models

# Create your models here.
class Transaction(models.Model):
    description = models.CharField(max_length=20)
    balance = models.IntegerField()
    debit =  models.IntegerField(null=True,blank=True)
    credit =  models.IntegerField(null=True,blank=True)
    status = models.CharField(max_length=1)

    @property
    def is_in_debit(self):
        return self.status == 'D'
    
    @property
    def is_in_credit(self):
        return self.status == 'C'