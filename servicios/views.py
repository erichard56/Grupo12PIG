from django.shortcuts import render, redirect
from servicios.models import Servicio

# Create your views here.
def servicios(request):
    servicios = Servicio.objects.all().order_by('-updated')
    return render(request, 'servicios/servicios.html', {"servicios":servicios})

def servicio_borrar(request, id):
    try:
        servicio = Servicio.objects.get(id = id)
    except:
        return redirect('/servicios')
    servicio.delete()
    return redirect('/servicios')
