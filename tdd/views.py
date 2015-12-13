
# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse

from django.template import RequestContext, loader
from django import template

import warnings

from django.conf import settings

from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.template.response import TemplateResponse
from django.utils.http import is_safe_url, urlsafe_base64_decode
from django.shortcuts import resolve_url
from tdd.models import Item,List

def view_list(request,list_id):
    list_=List.objects.get(id=list_id)
    return render(request,'tdd/list.html', {'list':list_} )

def new_list(request):
    list_=List.objects.create()
    Item.objects.create(text=request.POST['item_text'],list=list_)

    return redirect('/tdd/lists/%d/'%(list_.id)) 

def pag_inicio(request):
    return render(request,'tdd/pagina_inicio.html' )

def add_item(request,list_id):
    list_=List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'],list=list_)

    return redirect('/tdd/lists/%d/'%(list_.id)) 
