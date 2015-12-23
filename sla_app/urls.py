from django.conf.urls import url
from django.core.urlresolvers import reverse_lazy


from . import views 

urlpatterns = [
    #url(r'^index/$', views.index, name='index'),
    url(r'^$', views.home, name='home'),
    url(r'^profile/$', views.CompanyDetailView.as_view(), name='profile'),
    url(r'^profile/create/$', views.CompanyCreateView.as_view(success_url=reverse_lazy('profile')), name='profile-create'),
    url(r'^profile_update/$', views.profile_update, name='profile_update'),
    #url(r'^company/(?P<user_id>\d+)/$',views.view_company,name='view_company'),
    url(r'^company/(?P<user_id>\d+)/$',views.view_company.as_view(),name='view_company'),
    url(r'^company/(?P<user_id>\d+)/service_contract/$',views.create_service_contract,name='create_service_contract'),


    url(r'^company/(?P<user_id>\d+)/service_contract/(?P<list_id>\d+)/$',views.view_list,name='slapp_view_list'),
    url(r'^company/(?P<user_id>\d+)/service_contract/(?P<list_id>\d+)/add_item$',views.add_item,name='slapp_add_item'),

    url(r'^company/(?P<user_id>\d+)/service_contract/(?P<list_id>\d+)/delete/(?P<item_id>\d+)/$',views.delete_item,name='slapp_delete_item'),

]
