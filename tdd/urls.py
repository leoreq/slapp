from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^pag_inicio/$',views.pag_inicio,name='inicio'),
]
