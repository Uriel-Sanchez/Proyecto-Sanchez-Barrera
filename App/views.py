from http.client import HTTPResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from App.models import Autos, Motos, Propietario
from App.forms import Formulario_auto, Formulario_moto,Formulario_propietario,UserEditForm
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required





# Create you

def inicio(request):

    #return HttpResponse('estoy en el inicio')
    return render(request, "App/inicio.html")
@login_required
def autos(request):

    lista=Autos.objects.all()

    return render(request, "App/autos.html", {"lista": lista})
@login_required
def motos(request):

    lista=Motos.objects.all()

    return render(request, "App/motos.html", {"lista": lista})
@login_required
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


@login_required
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

@login_required
def busqueda_auto(request):

    return render(request, "App/busqueda_auto.html")

@login_required
def buscar_auto(request):

    if(request.method == 'GET'):

        marca= request.GET["marca"]
       
        autos=Autos.objects.filter(marca=marca)
    
        return render(request, "App/resultado_busqueda_auto.html", {"autos": autos, "marca": marca,})

    else:
        HttpResponse(f'No enviaste los datos')

    #return HttpResponse(f'Estamos buscando la marca y modelo {request.GET["marca"]} {request.GET["modelo"]}')


@login_required
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

@login_required
def formulario_propietario(request):

    if(request.method == 'POST'):

        formulario_propietario1 = Formulario_propietario(request.POST)

        if(formulario_propietario1.is_valid()):

            informacion= formulario_propietario1.cleaned_data

            propietario = Propietario(nombre=informacion["nombre"], apellido=informacion["apellido"], dni=informacion["dni"], email=informacion["email"], fechaDeAdquisicion=informacion["fechaDeAdquisicion"])

            propietario.save()

            return render(request, "App/inicio.html")

    else:

        formulario_propietario1= Formulario_propietario()

    return render(request, "App/formulario_propietario.html", {'form': formulario_propietario1})


def login_request(request):

    if(request.method == 'POST'):
        form = AuthenticationForm(request, data=request.POST)


        if(form.is_valid()):

            usuario= form.cleaned_data.get('username')
            contra= form.cleaned_data.get('password')
            
            user= authenticate(username=usuario, password=contra)

            if(user is not None):

                login(request, user)
                
                return render(request,"App/inicio.html", {'mensaje': f'Bienvenido {usuario}'})

            else:

                return render(request,"App/inicio.html", {'mensaje': f'Fallo la autenticacion, intentalo de nuevo'})

        else:

            return render(request,"App/inicio.html", {'mensaje': f'Formulario Erroneo, intentelo de nuevo'})


    else:
        form= AuthenticationForm()

        return render(request, "App/login.html", {'form': form})


def registrar(request):

    if(request.method == 'POST'):

        form = UserCreationForm(request.POST)

        if(form.is_valid()):

            username = form.cleaned_data['username']

            form.save()

            return render(request,"App/inicio.html", {'mensaje': f'Usuario creado, bienvenido {username}'})

        else:
            return redirect(registrar) #FALTARIA PONER UN TEXTO Q AVISE Q NO SE PUDO REGISTRAR EL USUARIO 

            #return render(request,"App/inicio.html", {'mensaje':'Error en los datos usuario no creado, intentelo de vuelta'})


    else:

        form = UserCreationForm()

    return render(request, "App/registrar.html", {'form': form})


@login_required
def buscar_moto(request):

    if(request.method == 'GET'):

        marca= request.GET["marca"]
       
        motos=Motos.objects.filter(marca=marca)
    
        return render(request, "App/resultado_busqueda_moto.html", {"motos": motos, "marca": marca,})

    else:
        HttpResponse(f'No enviaste los datos')

def editarPerfil(request):

    usuario = request.user

    if(request.method == 'POST'):

        miFormulario = UserEditForm(request.POST)

        if(miFormulario.is_valid()):

            informacion= miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.first_name = informacion['first_name']
            usuario.last_name = informacion['last_name']
            
            usuario.save()

            return render(request, "App/inicio.html")

    else:

        miFormulario= UserEditForm(initial={'email': usuario.email})

    return render(request, "App/editarPerfil.html", {'miFormulario': miFormulario, "usuario": usuario})

@login_required
def perfil(request):

    usuario = request.user

    return render(request, "App/perfil.html", {"usuario": usuario, "nombre": usuario.first_name, "apellido": usuario.last_name})


