from django.db import models

# Create your models here.

class Employee(models.Model):
    eid = models.CharField(max_length=30, unique=True)
    ename = models.CharField(max_length=30)
    eadd = models.CharField(max_length=100)  # 🔄 Increased from 30 to 100
    esal = models.IntegerField()
    ecity = models.CharField(max_length=30)
    eimg=models.FileField(upload_to='upload/', max_length=250, null=True, default=None)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)  # QR image

class Register(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=30)
    last_login = models.DateTimeField(null=True, blank=True)  # Optional: To track last login time
    
    def __str__(self):
        return self.email