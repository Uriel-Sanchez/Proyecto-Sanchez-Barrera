from xml.dom.minidom import Document
from django.conf import settings
from django.urls import path
from App import views
from django.contrib.auth.views import LogoutView
from django.conf.urls.static import static


urlpatterns = [

    path('',views.inicio, name="inicio"),
    path('about/',views.about,name="about"),
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

    path('formulario_mensaje/',views.formulario_mensaje,name="formulario_mensaje"),
    path('buzon_de_entrada/',views.buzon_de_entrada,name="buzon_de_entrada"),
    path('mensajes_enviados/',views.mensajes_enviados,name="mensajes_enviados"),

    path('foto_perfil/',views.foto_perfil,name="foto_perfil"),

    path('eliminar_moto/<id_moto>/',views.eliminar_moto,name="eliminar_moto"),
    path('eliminar_auto/<id_auto>/',views.eliminar_auto,name="eliminar_auto"),

    path('editar_moto/<id_moto>/',views.editar_moto,name="editar_moto"),
    path('editar_auto/<id_auto>/',views.editar_auto,name="editar_auto"),

    


    
    

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
