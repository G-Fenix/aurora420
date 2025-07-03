from . import views
from django.urls import path

urlpatterns = [
    path('', views.events),
    path('events', views.events),
    path('paintpuf-monday', views.paintpufmonday),
    path('highflix-tuesday', views.highflixtuesday),
    path('weedwisdom-wednesday', views.weedwisdomwednesday),
    path('talkit-thursday', views.talkitthursday),
    path('gamerush-friday', views.gamerushfriday),
    path('openmic-saturday', views.openmicsaturday),
]
