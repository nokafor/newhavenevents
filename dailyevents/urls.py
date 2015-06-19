from django.conf.urls import url

from dailyevents import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]


