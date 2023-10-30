"""
URL configuration for projeto_cad_usarios project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from app_cad_usuarios import views

urlpatterns = [
    #rota, view responsável, nome de referência
    #home.com
    path('', views.home, name='home'),
    #usuarios.com/usuarios
    path('usuarios/usuarios.html', views.usuarios, name='listagem_usuarios'),
    #info.com
    path('usuarios/info.html', views.info, name='informacoes'),
]