from django.contrib import admin
from .models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("pk", "first_name", "last_name", "patronymic", "image", "title", "hired_date", "parent")


admin.site.register(Employee, EmployeeAdmin)