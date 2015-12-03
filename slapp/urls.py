"""slapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin,auth
from django.contrib.auth import views
from sla_app import views

from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy




urlpatterns = [
    url(r'^pag_inicio/$',views.pag_inicio,name='inicio'),
	url(r'^slapp/', include('sla_app.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', auth.views.login, {'template_name': 'sla_app/login.html'},name='loginslap'),
    url(r'^password_reset/$', auth.views.password_reset, {'template_name': 'sla_app/password_reset_form.html'},name='pass_reset_form_slap'),
   	url('', include('django.contrib.auth.urls')),
    url('^register/', CreateView.as_view(
            template_name='register.html',
            form_class=UserCreationForm,
            success_url=reverse_lazy('profile_update')
    ),name='registerslap'),
    url('^accounts/', include('django.contrib.auth.urls')),
]
