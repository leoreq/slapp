from django.shortcuts import render
from django.http import HttpResponse

from django.template import RequestContext, loader

# Create your views here.


def pag_inicio():
    pass

def home(request):
    template = loader.get_template('sla_app/home.html')
    context = RequestContext(request, {
        'test': 'test',
    })
    return HttpResponse(template.render(context))

# Create your views here.


#def index(request):
#    return HttpResponse("This will hold the SLAPP Landing Page")