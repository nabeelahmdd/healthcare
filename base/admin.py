from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from base.models import (
    Doctor, Appointment
)
# Register your models here.


# Doctor register to admin
class DoctorAdmin(admin.ModelAdmin):
    list_display = (
        'specialty', 'get_email', 'get_first_name', 'get_last_name', 'get_phone_number',
    )
    search_fields = (
        'specialty',
    )

    def get_email(self, obj):
        return obj.user.email

    def get_first_name(self, obj):
        return obj.user.first_name

    def get_last_name(self, obj):
        return obj.user.last_name

    def get_phone_number(self, obj):
        return obj.user.phone_number


admin.site.register(Doctor, DoctorAdmin)

# Appointment register to admin


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'clinic', 'status', 'date', 'time')
    search_fields = ('patient', 'doctor', 'clinic', 'status', 'date', 'time')
    list_filter = ('date',)


admin.site.register(Appointment, AppointmentAdmin)
