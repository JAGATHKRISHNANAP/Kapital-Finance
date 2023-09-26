from django.db import models

# Create your models here.
class customer(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField(default=0)
    adress=models.CharField(max_length=30)
    mob= models.IntegerField(default=0)
    email=models.CharField(max_length=30)
    bank=models.CharField(max_length=30)
    branch= models.CharField(max_length=30)
    ifsc = models.CharField(max_length=30)
    acc_no=models.IntegerField(default=0)
    loanduration=models.CharField(max_length=30)
    loanapprove=models.DateField()
    currentamont=models.IntegerField(default=0)
    loanamount=models.IntegerField(default=0)
    emi=models.IntegerField(default=0)