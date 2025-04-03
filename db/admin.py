from django.contrib import admin

# Register your models here.

from db.models import Employee
from db.models import Register  # Make sure this matches your actual app and model


class EmployeeAdmin(admin.ModelAdmin):
	list_listview = ('eid','ename','eadd','esal','ecity','eimg')
admin.site.register(Employee,EmployeeAdmin)

class RegisterAdmin(admin.ModelAdmin):
	list_listview = ('name','email','password')
admin.site.register(Register,RegisterAdmin)