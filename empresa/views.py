from django.shortcuts import render
from django.http import HttpResponse
from .models import Tecnologias
# Create your views here.

def nova_empresa(request):
    techs= Tecnologias.objects.all()
    print(techs)
    return render(request,'nova_empresa.html', {'techs':techs})