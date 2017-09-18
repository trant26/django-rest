from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
# from . import views
from gara import views

app_name = 'gara'

urlpatterns = [
    # url(r'^$', views.index, name= 'index'),
    url(r'^register$', views.get_name),
    url(r'^car/$', views.CarList.as_view()),
    url(r'^car/(?P<pk>[0-9]+)/$', views.CarDetail.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
urlpatterns += [
    # url(r'^api-auth/', include('rest_framework.urls',
    #                            namespace='rest_framework')),
    url(r'^accounts/', include('django.contrib.auth.urls')),
]