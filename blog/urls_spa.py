from . import views
from django.urls import path

urlpatterns = [
    path('', views.icerik),
    path('blog', views.icerik),
]
