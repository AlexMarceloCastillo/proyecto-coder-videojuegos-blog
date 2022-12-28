from django.urls import path
from videojuegoapp import views

urlpatterns = [
    path("", views.inicio, name='Inicio')
]
