
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
from tdd.models import Item




def pag_inicio(request):
    if request.method=='POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')

    items=Item.objects.all()

    return render(request,'tdd/pagina_inicio.html', {'items':items} )


