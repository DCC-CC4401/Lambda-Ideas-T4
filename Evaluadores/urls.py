from django.urls import path
from . import views

urlpatterns = [
    path('evaluadores', views.post_evaluadores, name='evaluadores'),
    path('add_evaluador', views.add_evaluador, name='add_evaluador'),
    path('update_evaluador', views.update_evaluador, name='update_evaluador'),
    path('delete_evaluador', views.delete_evaluador, name='delete_evaluador'),
    path('profile', views.get_evaluador_profile, name='profile'),
]
