from django.shortcuts import render

from dailyevents.models import Calendar

# Create your views here.
def index(request):
    calendar = Calendar.objects.get(id=1)
    date = calendar.last_updated.date()

    calendar_list = Calendar.objects.all()

    return render(request, 'dailyevents/index.html', {'date':date, 'calendar_list':calendar_list})



