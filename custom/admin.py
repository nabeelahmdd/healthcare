from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from custom.models import (
    User, Clinic
)
# Register your models here.


# User register to admin
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'email', 'first_name', 'last_name', 'phone_number',
    )
    search_fields = (
        'email', 'first_name', 'last_name',  'phone_number',
    )
    list_filter = ('date_joined',)


admin.site.register(User, UserAdmin)


# Clinic register to admin
class ClinicAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'address_line_1', 'city', 'state', 'zip_code', 'country',
    )
    search_fields = (
        'name', 'address_line_1', 'city', 'state', 'zip_code', 'country',
    )
    list_filter = ('name',)


admin.site.register(Clinic, ClinicAdmin)
