"""
URL configuration for TercerraEntrega project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from appTerceraEntrega import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('post_list/', views.post_list, name="post_list"),
    path('productos/', views.productos, name="productos"),
    path('categorias/', views.categorias, name="categorias"),
    path('clientes/', views.clientes, name="clientes"),
    path('producto_formulario/', views.producto_formulario,name='producto_formulario'),
    path('categoria_formulario/', views.categoria_formulario,name='categoria_formulario'),
    path('cliente_formulario/', views.cliente_formulario,name='cliente_formulario'),
    path('busquedaProducto/', views.busquedaProducto, name="busquedaProducto"),
    path('buscar/', views.buscar, name='buscar'),
]
