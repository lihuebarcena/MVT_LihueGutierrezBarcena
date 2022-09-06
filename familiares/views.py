from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import Template, Context, loader
from familiares.models import Familiar

def listar_familiares(request):
    #Yo cargué los datos por consola por eso deberían estar cargados, no funciona así?
    #queryset=Familiar.objects.all()
    #diccio={'Familiar':queryset}
    user=Familiar(1,'primo','Pedro',22,'2000-10-10')
    user.save()

    diccio={'familiares':[familiares for familiares in Familiar.objects.values()]}

    plantilla=loader.get_template('familiares_list.html')
    documento_html=plantilla.render(diccio)
    
    return HttpResponse(documento_html)
