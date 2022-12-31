from django.urls import path
from django.contrib.auth.views import LogoutView
from videojuegoapp.views import *


urlpatterns = [
    path('', inicio, name='gameblog-home'),
    path('home', inicio, name='gameblog-home'),
    path('auth/register', register, name='gameblog-register'),
    path('auth/login', login, name='gameblog-login'),
    path('auth/profile', profile, name='gameblog-profile'),
    path('auth/logout', LogoutView.as_view(next_page="/home"), name='gameblog-logout'),
    # Admin
    path('actions', actions, name='gameblog-actions'),
    # CRUD Genero
    path('actions/create/genero', create_genero, name='gameblog-create-genero'),
    path('actions/list/genero/<int:page>', list_genero, name='gameblog-list-genero'),
    path('actions/update/genero/<int:id>', update_genero, name='gameblog-update-genero'),
    path('actions/delete/genero/<int:id>', delete_genero, name='gameblog-delete-genero'),
    # CRUD Plataforma
    path('actions/create/plataforma', create_plataforma, name='gameblog-create-plataforma'),
    path('actions/list/plataforma/<int:page>', list_plataforma, name='gameblog-list-plataforma'),
    path('actions/update/plataforma/<int:id>', update_plataforma, name='gameblog-update-plataforma'),
    path('actions/delete/plataforma/<int:id>', delete_plataforma, name='gameblog-delete-plataforma'),
    # CRUD Desarrollador
    path('actions/create/desarrollador', create_desarrollador, name='gameblog-create-desarrollador'),
    path('actions/list/desarrollador/<int:page>', list_desarrollador, name='gameblog-list-desarrollador'),
    path('actions/update/desarrollador/<int:id>', update_desarrollador, name='gameblog-update-desarrollador'),
    path('actions/delete/desarrollador/<int:id>', delete_desarrollador, name='gameblog-delete-desarrollador'),
    # CRUD Autor
    path('actions/create/autor', create_autor, name='gameblog-create-autor'),
    path('actions/list/autor/<int:page>', list_autor, name='gameblog-list-autor'),
    path('actions/update/autor/<int:id>', update_autor, name='gameblog-update-autor'),
    path('actions/delete/autor/<int:id>', delete_autor, name='gameblog-delete-autor'),
    # CRUD Post
    path('actions/create/post', create_post, name='gameblog-create-post'),
    path('actions/list/post/<int:page>', list_post, name='gameblog-list-post'),
    path('actions/update/post/<int:id>', update_post, name='gameblog-update-post'),
    path('actions/delete/post/<int:id>', delete_post, name='gameblog-delete-post'),
    # CRUD Categoria
    path('actions/create/categoria', create_categoria, name='gameblog-create-categoria'),
    path('actions/list/categoria/<int:page>', list_categoria, name='gameblog-list-categoria'),
    path('actions/update/categoria/<int:id>', update_categoria, name='gameblog-update-categoria'),
    path('actions/delete/categoria/<int:id>', delete_categoria, name='gameblog-delete-categoria'),
    # CRUD Videojuego
    path('actions/create/videojuego', create_videojuego, name='gameblog-create-videojuego'),
    path('actions/list/videojuego/<int:page>', list_videojuego, name='gameblog-list-videojuego'),
    path('actions/update/videojuego/<int:id>', update_videojuego, name='gameblog-update-videojuego'),
    path('actions/delete/videojuego/<int:id>', delete_videojuego, name='gameblog-delete-videojuego'),
]
