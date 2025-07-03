"""aurora URL Configuration

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
from django.shortcuts import render
from django.urls import include, path

def index(request):
    return render(request, 'en/index.html')

def paginaprincipal(request):
    return render(request, 'spa/paginaprincipal.html')
    


urlpatterns = [
    path('', paginaprincipal),
    path('en/', index),
    path('pagina-principal/', paginaprincipal),
    path('eventos/', include('events.urls_spa')),
    path('blog/', include('blog.urls_spa')),
    path('sobre-nosotros/', include('aboutus.urls_spa')),
    path('contactanos/', include('contactus.urls_spa')),
    path('en/index/', index),
    path('en/events/', include('events.urls_en')),
    path('en/blog/', include('blog.urls_en')),
    path('en/about-us/', include('aboutus.urls_en')),
    path('en/contact-us/', include('contactus.urls_en')),
    path('admin/', admin.site.urls),
]
