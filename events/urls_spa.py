from . import views
from django.urls import path

urlpatterns = [
    path('', views.eventos),
    path('eventos', views.eventos),
    path('lunes-de-pintura-y-caladas', views.lunesdepintura),
    path('martes-de-highflix', views.martesdehighflix),
    path('miercoles-de-sabiduria', views.miercolesdesabiduria),
    path('jueves-de-conversa', views.juevesdeconserva),
    path('viernes-de-juegos', views.viernesdejuegos),
    path('sabado-de-microfono', views.sabadodemicrofono),
]
