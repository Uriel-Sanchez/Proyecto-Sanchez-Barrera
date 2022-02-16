from http.client import HTTPResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from App.models import Autos, Motos, Propietario, Mensajeria, Foto_PerfilM
from App.forms import Formulario_auto, Formulario_moto,Formulario_propietario, UserEditForm, Formulario_mensaje,Foto_Perfil
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

def about(request):

	
    return render(request, "App/about.html")


# FORMULARIO CREADO PARA EL HTML ---- def formulario_auto(request):

    if(request.method == 'POST'):

        auto = Autos(marca=request.POST["marca"], modelo=request.POST["modelo"], color=request.POST["color"], km=request.POST["km"])

        auto.save()

        return render(request, "App/inicio.html")

    return render(request, "App/formulario_auto.html")


@login_required
def formulario_auto(request):

    if(request.method == 'POST'):

        formulario_auto1 = Formulario_auto(request.POST, request.FILES)

        if(formulario_auto1.is_valid()):

            informacion= formulario_auto1.cleaned_data

            auto = Autos(user=request.user, marca=informacion["marca"], modelo=informacion["modelo"], color=informacion["color"], km=informacion["km"], imagen= informacion["imagen"])

            auto.save()

            return render(request, "App/perfil.html")

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

        formulario_moto1 = Formulario_moto(request.POST, request.FILES)

        if(formulario_moto1.is_valid()):

            informacion= formulario_moto1.cleaned_data

            moto = Motos(user=request.user, marca=informacion["marca"], modelo=informacion["modelo"], color=informacion["color"], km=informacion["km"], imagen= informacion["imagen"])
            
            moto.save()

            return render(request, "App/perfil.html")

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

            return render(request, "App/perfil.html")

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
                
                #return render(request,"App/inicio.html", {'mensaje': f'Bienvenido {usuario}'})
                return redirect(perfil)
            else:

                return redirect(login_request)

                #return render(request,"App/login.html", {'mensaje': f'Fallo la autenticacion, intentalo de nuevo'})

        else:

            print(f'Formulario Erroneo, intentelo de nuevo')
 
            #return render(request,"App/login.html", {'mensaje': f'Formulario Erroneo, intentelo de nuevo'})
            return redirect(login_request)


    else:
        form= AuthenticationForm()

    return render(request, "App/login.html", {'form': form})


def registrar(request):

    if(request.method == 'POST'):

        form = UserCreationForm(request.POST)

        if(form.is_valid()):

            username = form.cleaned_data['username']

            form.save()

            return render(request,"App/perfil.html", {'mensaje': f'Usuario creado, bienvenido {username}'})

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

            return render(request, "App/perfil.html")

    else:

        miFormulario= UserEditForm(initial={'email': usuario.email})

    return render(request, "App/editarPerfil.html", {'miFormulario': miFormulario, "usuario": usuario})

@login_required
def perfil(request):

    usuario = request.user

    publicacionesA = Autos.objects.filter(user=request.user)

    publicacionesM = Motos.objects.filter(user=request.user)

    fotoP = Foto_PerfilM.objects.filter(user=request.user)

    return render(request, "App/perfil.html", {"usuario": usuario, "nombre": usuario.first_name, "apellido": usuario.last_name, "publicacionesA": publicacionesA, "publicacionesM": publicacionesM, "fotoP":fotoP})


@login_required
def formulario_mensaje(request):

    if(request.method == 'POST'):

        formulario_mensaje1 = Formulario_mensaje(request.POST)

        if(formulario_mensaje1.is_valid()):

            informacion= formulario_mensaje1.cleaned_data

            mensaje = Mensajeria(user=request.user, destinatario=informacion["destinatario"], mensaje=informacion["mensaje"])

            mensaje.save()

            return render(request, "App/perfil.html", {'mensaje': f'Mensaje enviado a {mensaje.destinatario} correctamente'})

    else:

        formulario_mensaje1= Formulario_mensaje()

    return render(request, "App/formulario_mensaje.html", {'form': formulario_mensaje1})
    

@login_required
def buzon_de_entrada(request):

    mensajes = Mensajeria.objects.filter(destinatario= request.user) 

    return render(request, "App/buzon_de_entrada.html", {'mensajes': mensajes})


@login_required
def mensajes_enviados(request):

    mensajes = Mensajeria.objects.filter(user= request.user.id) 

    return render(request, "App/mensajes_enviados.html", {'mensajes': mensajes})



@login_required
def foto_perfil(request):

    if(request.method == 'POST'):

        foto_perfil1 = Foto_Perfil(request.POST, request.FILES)

        if(foto_perfil1.is_valid()):

            informacion= foto_perfil1.cleaned_data

            foto = Foto_PerfilM(user=request.user, imagen= informacion["imagen"])
            
            foto.save()

            return render(request, "App/inicio.html")

    else:

        foto_perfil1= Foto_Perfil()

    return render(request, "App/foto_perfil.html", {'form': foto_perfil1})
    

@login_required
def eliminar_moto(request, id_moto):

    moto= Motos.objects.get(id=id_moto)

    moto.delete()

    motos= Motos.objects.all()
    
    return redirect(perfil)

    
@login_required
def eliminar_auto(request, id_auto):

    auto= Autos.objects.get(id=id_auto)

    auto.delete()

    autos= Autos.objects.all()
    
    return redirect(perfil)



@login_required
def editar_moto(request, id_moto):

    usuario = request.user

    moto= Motos.objects.get(id=id_moto)

    if(request.method == 'POST'):

        miFormulario = Formulario_moto(request.POST, request.FILES)

        if(miFormulario.is_valid()):

            informacion= miFormulario.cleaned_data

            moto.marca = informacion['marca']
            moto.modelo = informacion['modelo']
            moto.color = informacion['color']
            moto.km = informacion['km']
            moto.imagen = informacion['imagen']  
            
            moto.save()

            return redirect(perfil)

    else:

        miFormulario= Formulario_moto(initial={'marca': moto.marca, 'modelo':moto.modelo, 'color':moto.color, 'km':moto.km, 'imagen':moto.imagen})

    return render(request, "App/editar_moto.html", {'miFormulario': miFormulario, "id_moto": id_moto})
           

@login_required
def editar_auto(request, id_auto):

    usuario = request.user

    auto= Autos.objects.get(id=id_auto)

    if(request.method == 'POST'):

        miFormulario = Formulario_auto(request.POST, request.FILES)

        if(miFormulario.is_valid()):

            informacion= miFormulario.cleaned_data

            auto.marca = informacion['marca']
            auto.modelo = informacion['modelo']
            auto.color = informacion['color']
            auto.km = informacion['km']
            auto.imagen = informacion['imagen']  
            
            auto.save()

            return redirect(perfil)

    else:

        miFormulario= Formulario_moto(initial={'marca': auto.marca, 'modelo':auto.modelo, 'color':auto.color, 'km':auto.km, 'imagen':auto.imagen})

    return render(request, "App/editar_auto.html", {'miFormulario': miFormulario, "id_moto": id_auto})