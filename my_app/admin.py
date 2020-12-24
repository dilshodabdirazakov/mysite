from django.contrib import admin
from .models import *
# Register your models here.

class BoardAdmin(admin.ModelAdmin):
    list_display = ('dispatch', 'load_number', 'pickup_number', 'driver', 'phone_number', 'origin', 'delivery', 'mile', 'rate', 'broker')



admin.site.register(Board, BoardAdmin)