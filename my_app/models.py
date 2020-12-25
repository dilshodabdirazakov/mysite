from django.db import models

# Create your models here.
class COVERED_LOAD(models.Model):
    dispatch = models.CharField(max_length=255, default="")
    load_number = models.CharField(max_length=255, default="")
    pickup_number = models.CharField(max_length=255, default="")
    driver = models.CharField(max_length=255, default="")
    phone_number = models.CharField(max_length=1000, default="")
    origin = models.CharField(max_length=2080, default="")
    delivery = models.CharField(max_length=2080, default="")
    mile = models.CharField(max_length=2080, default="")
    rate = models.CharField(max_length=2080, default="")
    broker = models.CharField(max_length=500, default="")

class Update(models.Model):
	driver_name = models.CharField(max_length=300, default="")
	phone_number = models.CharField(max_length=500, default="")
	status = models.CharField(max_length=500, default="")
	first_note = models.CharField(max_length=500, default="")
	second_note = models.CharField(max_length=500, default="")


