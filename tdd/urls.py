from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^pag_inicio/$',views.pag_inicio,name='inicio'),
    url(r'^lists/new/$',views.new_list,name='new_list'),
    url(r'^lists/(\d+)/$',views.view_list,name='view_list'),
    url(r'^lists/(\d+)/add_item$',views.add_item,name='add_item'),

]
