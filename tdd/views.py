from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

from django.template import RequestContext, loader


import warnings

from django.conf import settings

from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.template.response import TemplateResponse
from django.utils.http import is_safe_url, urlsafe_base64_decode
from django.shortcuts import resolve_url

# Create your views here.


def pag_inicio(request):
    return render(request,'tdd/pagina_inicio.html',{'new_item_text':request.POST.get('item_text','')})

