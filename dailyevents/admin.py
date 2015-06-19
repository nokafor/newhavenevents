from django.contrib import admin
from dailyevents.models import Calendar

# Register your models here.
class CalendarAdmin(admin.ModelAdmin):
    list_display = ['name', 'last_updated', 'get_scraping_name']

admin.site.register(Calendar, CalendarAdmin)

