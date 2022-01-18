from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
from App.models import Autos, Motos, Propietario
from App.forms import Formulario_auto, Formulario_moto,Formulario_propietario


# Create your views here.

def inicio(request):

    #return HttpResponse('estoy en el inicio')
    return render(request, "App/inicio.html")

def autos(request):

    lista=Autos.objects.all()

    return render(request, "App/autos.html", {"lista": lista})

def motos(request):

    lista=Motos.objects.all()

    return render(request, "App/motos.html", {"lista": lista})

def propietarios(request):

    lista=Propietario.objects.all()

    return render(request, "App/propietarios.html", {"lista": lista})

def saludo(request):

	#return HttpResponse("saludoo")
    return render(request, "App/saludo.html")


# FORMULARIO CREADO PARA EL HTML ---- def formulario_auto(request):

    if(request.method == 'POST'):

        auto = Autos(marca=request.POST["marca"], modelo=request.POST["modelo"], color=request.POST["color"], km=request.POST["km"])

        auto.save()

        return render(request, "App/inicio.html")

    return render(request, "App/formulario_auto.html")



def formulario_auto(request):

    if(request.method == 'POST'):

        formulario_auto1 = Formulario_auto(request.POST)

        if(formulario_auto1.is_valid()):

            informacion= formulario_auto1.cleaned_data

            auto = Autos(marca=informacion["marca"], modelo=informacion["modelo"], color=informacion["color"], km=informacion["km"])

            auto.save()

            return render(request, "App/inicio.html")

    else:

        formulario_auto1= Formulario_auto()

    return render(request, "App/formulario_auto.html", {'form': formulario_auto1})


def busqueda_auto(request):

    return render(request, "App/busqueda_auto.html")


def buscar_auto(request):

    if(request.method == 'GET'):

        marca= request.GET["marca"]
        
        autos=Autos.objects.filter(marca=marca)
        
        return render(request, "App/resultado_busqueda_auto.html", {"autos": autos, "marca": marca})

    else:
        HttpResponse(f'No enviaste los datos')

    #return HttpResponse(f'Estamos buscando la marca y modelo {request.GET["marca"]} {request.GET["modelo"]}')


def formulario_moto(request):

    if(request.method == 'POST'):

        formulario_moto1 = Formulario_moto(request.POST)

        if(formulario_moto1.is_valid()):

            informacion= formulario_moto1.cleaned_data

            moto = Motos(marca=informacion["marca"], modelo=informacion["modelo"], color=informacion["color"], km=informacion["km"])

            moto.save()

            return render(request, "App/inicio.html")

    else:

        formulario_moto1= Formulario_moto()

    return render(request, "App/formulario_moto.html", {'form': formulario_moto1})


def formulario_propietario(request):

    if(request.method == 'POST'):

        formulario_propietario1 = Formulario_propietario(request.POST)

        if(formulario_propietario1.is_valid()):

            informacion= formulario_propietario1.cleaned_data

            propietario = Propietario(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"], fechaDeAdquisicion=informacion["fechaDeAdquisicion"])

            propietario.save()

            return render(request, "App/inicio.html")

    else:

        formulario_propietario1= Formulario_propietario()

    return render(request, "App/formulario_propietario.html", {'form': formulario_propietario1})
