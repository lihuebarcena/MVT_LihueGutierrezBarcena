from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import Template, Context, loader
from familiares.models import familiares

def listar_familiares(request):
    #Yo cargué los datos por consola por eso deberían estar cargados, no funciona así?
    # queryset=familiares.objects.all()
    #diccio={'familiares':queryset}
    user=familiares('primo','Pedro',22,'2000-10-10')
    user.save()

    diccio={'familiares':[familiares for familiares in familiares.objects.values()]}

    plantilla=loader.get_template('familiares_list.html')
    documento_html=plantilla.render(diccio)
    
    return HttpResponse(documento_html)
