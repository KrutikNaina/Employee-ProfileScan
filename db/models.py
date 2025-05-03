from django.db import models

# Create your models here.

# class Employee(models.Model):
#     eid = models.CharField(max_length=30, unique=True)
#     ename = models.CharField(max_length=30)
#     eadd = models.CharField(max_length=100)  # 🔄 Increased from 30 to 100
#     esal = models.IntegerField()
#     ecity = models.CharField(max_length=30)
#     eimg=models.FileField(upload_to='upload/', max_length=250, null=True, default=None)
#     qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)

from django.utils import timezone


class Register(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=30)
    last_login = models.DateTimeField(null=True, blank=True)  # Optional: To track last login time
    
    def __str__(self):
        return self.email

class Employee(models.Model):
    eid = models.CharField(max_length=10, primary_key=True)
    ename = models.CharField(max_length=100)
    eadd = models.CharField(max_length=255)
    esal = models.DecimalField(max_digits=10, decimal_places=2)
    ecity = models.CharField(max_length=50)
    eimg = models.ImageField(upload_to='employee_images/', null=True, blank=True)  # Modify this line to set a default value
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)

    def __str__(self):
        return self.ename

class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    status = models.CharField(max_length=10, choices=[('present', 'Present'), ('absent', 'Absent')], default='absent')
    time_in = models.TimeField(null=True, blank=True)
    time_out = models.TimeField(null=True, blank=True)

    def __str__(self):
        return f"Attendance for {self.employee.ename} on {self.date}"
