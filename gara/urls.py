from django.conf.urls import url

# from . import views
from gara import views

app_name = 'gara'

urlpatterns = [
    # url(r'^$', views.index, name= 'index'),
    # url(r'^register$', views.register),
    url(r'^car/$', views.car_list),
    url(r'^car/(?P<pk>[0-9]+)/$', views.car_detail),
]

 