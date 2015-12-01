from django.conf.urls import url

from . import views

urlpatterns = [
    #url(r'^index/$', views.index, name='index'),
    url(r'^$', views.home, name='home'),
    url(r'^profile_update$', views.profile_update, name='profile_update'),
]
