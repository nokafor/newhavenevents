import datetime

from django.db import models
from django.utils import timezone

from dailyevents import functions

# Create your models here.
class Calendar(models.Model):
    name = models.CharField(max_length=200)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
    	ordering = ['name']

    def __str__(self):
    	return self.name

    def get_scraping_name(self):
    	return "getEvents%s" % self.id
    
    def get_events(self):
    	# function_name = 

    	events = getattr(functions, "get_events%s" % self.id)()

    	return events



