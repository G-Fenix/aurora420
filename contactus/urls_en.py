from . import views
from django.urls import path

urlpatterns = [
    path('', views.contactus),
    path('contact-us', views.contactus),
]
