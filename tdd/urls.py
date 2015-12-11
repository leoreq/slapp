from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^pag_inicio/$',views.pag_inicio,name='inicio'),
    url(r'^lists/new/$',views.new_list,name='new_list'),
    url(r'^lists/the-only-list-in-the-world/$',views.view_list,name='view_list'),
]
