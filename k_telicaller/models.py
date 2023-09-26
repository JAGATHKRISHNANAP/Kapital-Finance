from django.db import models
from k_employee.models import customer
from k_admin.models import empreg

# Create your models here.
class telefb(models.Model):
    feedback=models.CharField(max_length=50)
    cust=models.ForeignKey(customer,on_delete=models.CASCADE)
    emp=models.ForeignKey(empreg,on_delete=models.CASCADE)

