from django.conf.urls import url

from . import views

app_name = 'log'
urlpatterns = [
    url(r'^update/(?P<latitude>[-+]?[0-9]*\.?[0-9]+)/(?P<longitude>[-+]?[0-9]*\.?[0-9]+)/(?P<battery_v>[-+]?[0-9]*\.?[0-9]+)/(?P<pumping>[-+]?[0-9]*\.?[0-9]+)/$', views.update, name='update'),
]
