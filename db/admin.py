from django.contrib import admin

# Register your models here.

from db.models import Employee


class EmployeeAdmin(admin.ModelAdmin):
	list_listview = ('eid','ename','eadd','esal','ecity','eimg')
admin.site.register(Employee,EmployeeAdmin)