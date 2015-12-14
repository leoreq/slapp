from django.conf.urls import url
from django.core.urlresolvers import reverse_lazy


from . import views 

urlpatterns = [
    #url(r'^index/$', views.index, name='index'),
    url(r'^$', views.home, name='home'),
    url(r'^profile/$', views.CompanyDetailView.as_view(), name='profile'),
    url(r'^profile/create/$', views.CompanyCreateView.as_view(success_url=reverse_lazy('profile')), name='profile-create'),
    url(r'^profile_update/$', views.profile_update, name='profile_update'),
    url(r'^company/(\d+)/$',views.view_company,name='view_company'),
]
'lists/(\d+)/$'