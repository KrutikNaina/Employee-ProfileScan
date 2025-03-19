from django.db import models

# Create your models here.

class Employee(models.Model):
    eid = models.CharField(max_length=30)
    ename = models.CharField(max_length=30)
    eadd = models.CharField(max_length=30)
    esal = models.IntegerField()
    ecity = models.CharField(max_length=30)
    eimg=models.FileField(upload_to='upload/', max_length=250, null=True, default=None)