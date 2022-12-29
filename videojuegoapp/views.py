from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as login_
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from videojuegoapp.models import *
from videojuegoapp.forms import *


def inicio(request):
    return render(request, "videojuego/index/index.html")

# Auth Views
def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login_(request, new_user)
            return render(request, "videojuego/index/index.html")
    else:
        form = UserForm()

    return render(request, "videojuego/auth/register.html", {"form": form})


def login(request):

    errors = ''

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            data = form.cleaned_data

            user = authenticate(
                username=data["username"], password=data["password"])
            if user is not None:
                login_(request, user)
                return redirect('/home')
            else:
                return render(request, 'videojuego/auth/login.html', {"form": form, "errors": "Credenciales invalidas"})
        else:
            return render(request, 'videojuego/auth/login.html', {"form": form, "errors": form.errors})
    form = AuthenticationForm()
    return render(request, 'videojuego/auth/login.html', {"form": form, "errors": errors})


@login_required
def profile(request):
    return render(request, "videojuego/auth/profile.html")
