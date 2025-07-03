from . import views
from django.urls import path

urlpatterns = [
    path('', views.sobrenosotros),
    path('sobre-nosotros', views.sobrenosotros),
    
]
