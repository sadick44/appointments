from django.contrib import admin
from .models import Appointment


class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_created', 'appointement_date']


admin.site.register(Appointment, AppointmentAdmin)
