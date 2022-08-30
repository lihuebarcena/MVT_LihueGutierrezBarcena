from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import Template, Context, loader
from familiares.models import familiares

def listar_familiares(request):
    queryset=familiares.objects.all()
    diccio={'familiares':queryset}
    plantilla=loader.get_template('familiares_list.html')
    documento_html=plantilla.render(diccio)
    return HttpResponse(documento_html)
