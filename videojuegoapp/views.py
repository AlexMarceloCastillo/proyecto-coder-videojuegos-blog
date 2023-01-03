from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as login_
from django.shortcuts import redirect
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required, user_passes_test
from datetime import datetime

from videojuegoapp.models import *
from videojuegoapp.forms import *


def check_admin(user):
    return user.is_superuser

# Home


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
            return redirect('/home')
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
                if user.is_superuser:
                    return redirect('/actions')
                return redirect('/home')
            else:
                return render(request, 'videojuego/auth/login.html', {"form": form, "errors": "Error al loguearse"})
        else:
            return render(request, 'videojuego/auth/login.html', {"form": form, "errors": form.errors})
    form = AuthenticationForm()
    return render(request, 'videojuego/auth/login.html', {"form": form, "errors": errors})

@login_required
def profile(request):
    user = request.user
    if request.method == "POST":
        form = FormEditProfile(request.POST)
        if form.is_valid():
                data = form.cleaned_data
                user.first_name = data['first_name']
                user.last_name = data['last_name']
                user.email = data['email']
                user.username = data['username']
                user.save()
                return redirect('/auth/profile')
    else:
        form = FormEditProfile(initial ={'first_name':user.first_name, 'last_name':user.last_name, 'email':user.email, 'username':user.username})
    return render(request, 'videojuego/auth/profile.html', {"form": form})

@login_required
def profile_password(request):
    user = request.user
    if request.method == "POST":
        form = FormEditPassword(request.POST)
        if form.is_valid():
                data = form.cleaned_data
                if data["password1"] != data["password2"]:
                    return render(request, 'videojuego/auth/edit-password.html', {"form": form, "errors": 'Las contraseñas deben ser iguales'})
                user.set_password(data["password1"])
                user.save()
                return redirect('/auth/profile')
    else:
        form = FormEditPassword()
    return render(request, 'videojuego/auth/edit-password.html', {"form": form})
# End Auth Views

# ----------------------------------------------

# Admin Views


@login_required
@user_passes_test(check_admin)
def actions(request):
    return render(request, 'videojuego/crud/actions.html')

# CRUD Genero
@login_required
@user_passes_test(check_admin)
def list_genero(request, page):
    generos = Genero.objects.all()
    paginator = Paginator(generos, per_page=5)
    page_genero = paginator.get_page(page)
    return render(request, 'videojuego/crud/genero/list.html', {'page_genero': page_genero})


@login_required
@user_passes_test(check_admin)
def create_genero(request):
    if request.method == "POST":
        form = CreateFormGenero(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            genero = Genero(nombre=data["nombre"],
                            fecha_creacion=datetime.now())
            genero.save()
            return redirect('/actions/list/genero/1')
    else:
        form = CreateFormGenero()
    return render(request, 'videojuego/crud/genero/create.html', {"form": form})


@login_required
@user_passes_test(check_admin)
def update_genero(request, id):
    genero = Genero.objects.get(id=id)
    if request.method == "POST":
        form = UpdateFormGenero(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            genero.nombre = data["nombre"]
            genero.fecha_creacion = data["fecha_creacion"]
            genero.save()
            return redirect('/actions/list/genero/1')
    else:
        data_mapped = {}
        data_mapped["nombre"] = genero.nombre
        data_mapped["fecha_creacion"] = genero.fecha_creacion
        form = UpdateFormGenero(data=data_mapped)
    return render(request, 'videojuego/crud/genero/update.html', {"form": form})


@login_required
@user_passes_test(check_admin)
def delete_genero(request, id):
    genero = Genero.objects.get(id=id)
    genero.delete()
    return redirect('/actions/list/genero/1')

# End CRUD Genero

# CRUD Plataforma


@login_required
@user_passes_test(check_admin)
def list_plataforma(request, page):
    plataformas = Plataforma.objects.all()
    paginator = Paginator(plataformas, per_page=5)
    page_plataforma = paginator.get_page(page)
    return render(request, 'videojuego/crud/plataforma/list.html', {'page_plataforma': page_plataforma})


@login_required
@user_passes_test(check_admin)
def create_plataforma(request):
    if request.method == "POST":
        form = FormPlataforma(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            plataforma = Plataforma(nombre=data["nombre"],
                                    fecha_lanzamiento=data["fecha_lanzamiento"])
            plataforma.save()
            return redirect('/actions/list/plataforma/1')
    else:
        form = FormPlataforma()
    return render(request, 'videojuego/crud/plataforma/create.html', {"form": form})


@login_required
@user_passes_test(check_admin)
def update_plataforma(request, id):
    plataforma = Plataforma.objects.get(id=id)
    if request.method == "POST":
        form = FormPlataforma(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            plataforma.nombre = data["nombre"]
            plataforma.fecha_lanzamiento = data["fecha_lanzamiento"]
            plataforma.save()
            return redirect('/actions/list/plataforma/1')
    else:
        data_mapped = {}
        data_mapped["nombre"] = plataforma.nombre
        data_mapped["fecha_lanzamiento"] = plataforma.fecha_lanzamiento
        form = FormPlataforma(data=data_mapped)
    return render(request, 'videojuego/crud/plataforma/update.html', {"form": form})


@login_required
@user_passes_test(check_admin)
def delete_plataforma(request, id):
    plataforma = Plataforma.objects.get(id=id)
    plataforma.delete()
    return redirect('/actions/list/plataforma/1')
# End CRUD Plataforma

# CRUD Desarrollador
@login_required
@user_passes_test(check_admin)
def list_desarrollador(request, page):
    desarrolladores = Desarrollador.objects.all()
    paginator = Paginator(desarrolladores, per_page=5)
    page_desarrollador = paginator.get_page(page)
    return render(request, 'videojuego/crud/desarrollador/list.html', {'page_desarrollador': page_desarrollador})


@login_required
@user_passes_test(check_admin)
def create_desarrollador(request):
    if request.method == "POST":
        form = FormDesarrollador(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            desarrollador = Desarrollador(
                nombre=data["nombre"],
                fundacion=data["fundacion"],
                web_url=data["web_url"])
            desarrollador.save()
            return redirect('/actions/list/desarrollador/1')
    else:
        form = FormDesarrollador()
    return render(request, 'videojuego/crud/desarrollador/create.html', {"form": form})


@login_required
@user_passes_test(check_admin)
def update_desarrollador(request, id):
    desarrollador = Desarrollador.objects.get(id=id)
    if request.method == "POST":
        form = FormDesarrollador(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            desarrollador.nombre = data["nombre"]
            desarrollador.fundacion = data["fundacion"]
            desarrollador.web_url = data["web_url"]
            desarrollador.save()
            return redirect('/actions/list/desarrollador/1')
    else:
        data_mapped = {}
        data_mapped["nombre"] = desarrollador.nombre
        data_mapped["fundacion"] = desarrollador.fundacion
        data_mapped["web_url"] = desarrollador.web_url
        form = FormDesarrollador(data=data_mapped)
    return render(request, 'videojuego/crud/desarrollador/update.html', {"form": form})


@login_required
@user_passes_test(check_admin)
def delete_desarrollador(request, id):
    desarrollador = Desarrollador.objects.get(id=id)
    desarrollador.delete()
    return redirect('/actions/list/desarrollador/1')
# End CRUD Desarrollador

# CRUD Autor
@login_required
@user_passes_test(check_admin)
def list_autor(request, page):
    autores = Autor.objects.all()
    paginator = Paginator(autores, per_page=5)
    page_autor = paginator.get_page(page)
    return render(request, 'videojuego/crud/autor/list.html', {'page_autor': page_autor})

@login_required
@user_passes_test(check_admin)
def create_autor(request):
    if request.method == "POST":
        form = FormAutor(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User(
                username=data["username"],
                first_name=data["first_name"],
                last_name=data["last_name"],
                is_superuser=0,
                is_staff=0,
                email=data["email"],
                password=make_password(data["password1"])
            )
            user.save()
            autor = Autor(
                fecha_nacimiento=data["fecha_nacimiento"],
                foto_url=data["foto_url"],
                user=user
                )
            autor.save()
            return redirect('/actions/list/autor/1')
    else:
        form = FormAutor()
    return render(request, 'videojuego/crud/autor/create.html', {"form": form})

@login_required
@user_passes_test(check_admin)
def update_autor(request, id):
    autor = Autor.objects.get(id=id)
    if request.method == "POST":
        form = FormAutor(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            autor.nombre = data["nombre"]
            autor.fecha_nacimiento = data["fecha_nacimiento"]
            autor.foto_url = data["foto_url"]
            autor.save()
            return redirect('/actions/list/autor/1')
    else:
        data_mapped = {}
        data_mapped["nombre"] = autor.nombre
        data_mapped["apellido"] = autor.apellido
        data_mapped["foto_url"] = autor.foto_url
        data_mapped["fecha_nacimiento"] = autor.fecha_nacimiento
        form = FormAutor(data=data_mapped)
    return render(request, 'videojuego/crud/autor/update.html', {"form": form})

@login_required
@user_passes_test(check_admin)
def delete_autor(request, id):
    autor = Autor.objects.get(id=id)
    user = User.objects.get(id=autor.user.pk)
    user.delete()
    autor.delete()
    return redirect('/actions/list/autor/1')
# END CRUD Autor

# CRUD Post
@login_required
@user_passes_test(check_admin)
def list_post(request, page):
    posts = Post.objects.all()
    paginator = Paginator(posts, per_page=5)
    page_post = paginator.get_page(page)
    return render(request, 'videojuego/crud/post/list.html', {'page_post': page_post})

@login_required
@user_passes_test(check_admin)
def create_post(request):
    if request.method == "POST":
        form = FormPost(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            autor = Autor.objects.get(id=data["autor"])
            categoria = Categoria.objects.get(id=data["categoria"])
            post = Post(
                titulo=data["titulo"],
                subtitulo=data["subtitulo"],
                contenido=data["contenido"],
                fecha_creacion=datetime.now(),
                autor=autor,
                categoria=categoria,
                imagen_url=data["imagen_url"]
                )
            post.save()
            return redirect('/actions/list/post/1')
    else:
        form = FormPost()
    return render(request, 'videojuego/crud/post/create.html', {"form": form})

@login_required
@user_passes_test(check_admin)
def update_post(request, id):
    post = Post.objects.get(id=id)
    if request.method == "POST":
        form = FormPost(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            post.titulo = data["titulo"]
            post.subtitulo = data["subtitulo"]
            post.contenido = data["contenido"]
            post.imagen_url = data["imagen_url"]
            autor = Autor.objects.get(id=data["autor"])
            categoria = Categoria.objects.get(id=data["categoria"])
            post.autor = autor
            post.categoria = categoria
            post.save()
            return redirect('/actions/list/post/1')
    else:
        data_mapped = {}
        data_mapped["titulo"] = post.titulo
        data_mapped["subtitulo"] = post.subtitulo
        data_mapped["contenido"] = post.contenido
        data_mapped["imagen_url"] = post.imagen_url
        data_mapped["autor"] = post.autor.id
        data_mapped["categoria"] = post.categoria.id
        form = FormPost(data=data_mapped)
    return render(request, 'videojuego/crud/post/update.html', {"form": form})

@login_required
@user_passes_test(check_admin)
def delete_post(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('/actions/list/post/1')
# END CRUD Post

# CRUD Videojuego
@login_required
@user_passes_test(check_admin)
def list_videojuego(request, page):
    videojuegos = Videojuego.objects.all()
    paginator = Paginator(videojuegos, per_page=5)
    page_videojuego = paginator.get_page(page)
    return render(request, 'videojuego/crud/videojuego/list.html', {'page_videojuego': page_videojuego})

@login_required
@user_passes_test(check_admin)
def create_videojuego(request):
    if request.method == "POST":
        form = FormVideojuego(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            videojuego = Videojuego(
                nombre=data["nombre"],
                genero=Genero.objects.get(id=data["genero"]),
                desarrollador=Desarrollador.objects.get(id=data["desarrollador"]),
                fecha_lanzamiento=data["fecha_lanzamiento"]
                )
            videojuego.save()
            list_plataformas = data["plataformas"]
            for plataforma in list_plataformas:
                videojuego.plataformas.add(plataforma)           
            videojuego.save()
            return redirect('/actions/list/videojuego/1')
    else:
        form = FormVideojuego()
    return render(request, 'videojuego/crud/videojuego/create.html', {"form": form})

@login_required
@user_passes_test(check_admin)
def update_videojuego(request, id):
    videojuego = Videojuego.objects.get(id=id)
    if request.method == "POST":
        form = FormVideojuego(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            videojuego.nombre = data["nombre"]
            videojuego.genero = Genero.objects.get(id=data["genero"])
            videojuego.desarrollador = Desarrollador.objects.get(id=data["desarrollador"])
            videojuego.fecha_lanzamiento = data["fecha_lanzamiento"]
            videojuego.plataformas.set([])
            for plataforma in data["plataformas"]:
                videojuego.plataformas.add(plataforma)  
            videojuego.save()
            return redirect('/actions/list/videojuego/1')
    else:
        data_mapped = {}
        data_mapped["nombre"] = videojuego.nombre
        data_mapped["genero"] = videojuego.genero.id
        data_mapped["desarrollador"] = videojuego.desarrollador.id
        data_mapped["fecha_lanzamiento"] = videojuego.fecha_lanzamiento
        data_mapped["plataformas"] = [x.pk for x in videojuego.plataformas.all()]
        form = FormVideojuego(data=data_mapped)
    return render(request, 'videojuego/crud/videojuego/update.html', {"form": form})

@login_required
@user_passes_test(check_admin)
def delete_videojuego(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('/actions/list/post/1')
# END CRUD Videojuego

# CRUD Categoria
@login_required
@user_passes_test(check_admin)
def list_categoria(request, page):
    categorias = Categoria.objects.all()
    paginator = Paginator(categorias, per_page=5)
    page_categoria = paginator.get_page(page)
    return render(request, 'videojuego/crud/categoria/list.html', {'page_categoria': page_categoria})

@login_required
@user_passes_test(check_admin)
def create_categoria(request):
    if request.method == "POST":
        form = FormCategoria(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            categoria = Categoria(
                nombre=data["nombre"],
                )
            categoria.save()
            return redirect('/actions/list/categoria/1')
    else:
        form = FormCategoria()
    return render(request, 'videojuego/crud/categoria/create.html', {"form": form})

@login_required
@user_passes_test(check_admin)
def update_categoria(request, id):
    categoria = Categoria.objects.get(id=id)
    if request.method == "POST":
        form = FormCategoria(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            categoria.nombre = data["nombre"]
            categoria.save()
            return redirect('/actions/list/categoria/1')
    else:
        data_mapped = {}
        data_mapped["nombre"] = categoria.nombre
        form = FormCategoria(data=data_mapped)
    return render(request, 'videojuego/crud/categoria/update.html', {"form": form})

@login_required
@user_passes_test(check_admin)
def delete_categoria(request, id):
    categoria = Categoria.objects.get(id=id)
    categoria.delete()
    return redirect('/actions/list/categoria/1')
# END CRUD Categoria


# End Admin views
