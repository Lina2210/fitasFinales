from django.shortcuts import render
from .models import *
def automobil(request):
    autos = Automobil.objects.all()
    return render(request, 'autos.html', {'autos': autos}) 