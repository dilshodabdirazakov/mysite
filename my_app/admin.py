from django.contrib import admin
from .models import *
# Register your models here.

class UpdateAdmin(admin.ModelAdmin):
    list_dislay = ('driver_name', 'phone_number', 'status', 'first_note', 'second_note')

class COVERED_LOADAdmin(admin.ModelAdmin):
    list_display = ('dispatch', 'load_number', 'pickup_number', 'driver', 'phone_number', 'origin', 'delivery', 'mile', 'rate', 'broker')




admin.site.register(Update, UpdateAdmin)
admin.site.register(COVERED_LOAD, COVERED_LOADAdmin)
