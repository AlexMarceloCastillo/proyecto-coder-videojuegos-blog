from django.urls import path
from django.contrib.auth.views import LogoutView
from videojuegoapp.views import *


urlpatterns = [
    path('', inicio, name='gameblog-home'),
    path('home', inicio, name='gameblog-home'),
    path('auth/register', register, name='gameblog-register'),
    path('auth/login', login, name='gameblog-login'),
    path('auth/profile', profile, name='gameblog-profile'),
    path('auth/logout', LogoutView.as_view(next_page="/home"), name='gameblog-logout')
]
