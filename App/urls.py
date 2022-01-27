from django.urls import path
from App import views
from django.contrib.auth.views import LogoutView


urlpatterns = [

    path('',views.inicio, name="inicio"),
    path('saludo/',views.saludo,name="saludo"),
    path('autos/',views.autos,name="autos"),
    path('motos/',views.motos,name="motos"),
    path('propietarios/',views.propietarios,name="propietarios"),
    path('formulario_auto/',views.formulario_auto,name="formulario_auto"),
    path('busqueda_auto/',views.busqueda_auto,name="busqueda_auto"),
    path('buscar_auto/',views.buscar_auto,name="buscar_auto"),
    path('formulario_moto/',views.formulario_moto,name="formulario_moto"),
    path('formulario_propietario/',views.formulario_propietario,name="formulario_propietario"),

    path('login/',views.login_request,name="login"),
    path('registrar/',views.registrar,name="registrar"),
    path('logout/',LogoutView.as_view(template_name='App/logout.html'),name="logout"),

    path('buscar_moto/',views.buscar_moto,name="buscar_moto"),

    path('editarPerfil/',views.editarPerfil,name="editarPerfil"),
    path('perfil/',views.perfil,name="perfil"),
    

]