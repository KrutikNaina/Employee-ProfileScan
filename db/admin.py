from django.contrib import admin

# Register your models here.
from django.utils.html import format_html
from db.models import Employee
from db.models import Register  # Make sure this matches your actual app and model

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('eid', 'ename', 'ecity', 'esal', 'display_qr_code')

    readonly_fields = ('display_qr_code',)  # Show QR code in admin form (read-only)

    def display_qr_code(self, obj):
        if obj.qr_code:
            return format_html('<img src="{}" width="100" height="100" />', obj.qr_code.url)
        return "No QR Code"
    display_qr_code.short_description = 'QR Code'

admin.site.register(Employee, EmployeeAdmin)

# class EmployeeAdmin(admin.ModelAdmin):
# 	list_listview = ('eid','ename','eadd','esal','ecity','eimg')
# admin.site.register(Employee,EmployeeAdmin)

class RegisterAdmin(admin.ModelAdmin):
	list_listview = ('name','email','password')
admin.site.register(Register,RegisterAdmin)