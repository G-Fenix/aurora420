from . import views
from django.urls import path

urlpatterns = [
    path('', views.aboutus),
    path('about-us', views.aboutus),
    
]
