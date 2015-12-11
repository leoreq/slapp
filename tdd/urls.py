from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^pag_inicio/$',views.pag_inicio,name='inicio'),
    url(r'^pag_inicio/lists/the-only-list-in-the-world/$',views.view_list,name='view_list'),
]
