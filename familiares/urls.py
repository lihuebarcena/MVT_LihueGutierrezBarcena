from django.urls import path
from familiares.views import listar_familiares


urlpatterns = [
    path('', listar_familiares),
]