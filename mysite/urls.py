"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    # usamos el include para agregar las rutas que vienen de la carpeta myapp
    # si dejamos las comillas vacias no hay que tipear ninguna ruta extra, solo las que estan especificadas en la carpeta myapp, si le agregamos alguna, primero tipeamos esa y despues las que especificamos en la carpeta myapp
    path('', include("myapp.urls")),
    
]
