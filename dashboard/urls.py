from django.conf.urls import url

from . import views

app_name = 'dashboard'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<reading_id>[0-9]+)/$', views.index, name='index'),
]
