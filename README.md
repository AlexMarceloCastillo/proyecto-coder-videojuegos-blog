# Videojuego Blog

Proyecto final del curso de Python de CODERHOUSE

¿Que es Videojuego Blog?. Es una pagina blog dedicada a toda la informacion de la cultura de los videojuegos (noticias, lanzamientos, tv-series, etc)


#Rutas
--------------------------------------------------------------------

/home

/auth/login

/auth/register

/auth/logout

/post/query

/post/<id>

/auth/profile

/auth/profile/change-password

# Rutas ADMIN:
--------------------------------------------------------------------

Para loguearse como admin:

usuario: admin

contraseña: 12345678

#RUTA Principal
--------------------------------------------------------------------

actions


CRUD de Videojuegos
--------------------------------------------------------------------

actions/create/videojuego

actions/list/videojuego/<int:page>

actions/update/videojuego/<int:id>

actions/delete/videojuego/<int:id>

CRUD de Post
--------------------------------------------------------------------

actions/create/post

actions/list/post/<int:page>

actions/update/post/<int:id>

actions/delete/post/<int:id>

CRUD de Plataformas
--------------------------------------------------------------------

actions/create/plataforma

actions/list/plataforma/<int:page>

actions/update/plataforma/<int:id>

actions/delete/plataforma/<int:id>

CRUD de Categoria
--------------------------------------------------------------------

actions/create/categoria

actions/list/categoria/<int:page>

actions/update/categoria/<int:id>

actions/delete/categoria/<int:id>

CRUD de Desarrollador
--------------------------------------------------------------------

actions/create/desarrollador

actions/list/desarrollador/<int:page>

actions/update/desarrollador/<int:id>

actions/delete/desarrollador/<int:id>

CRUD de Autor
--------------------------------------------------------------------

actions/create/autor

actions/list/autor/<int:page>

actions/update/autor/<int:id>,

actions/delete/autor/<int:id>

CRUD de Genero (de Videojuego)
--------------------------------------------------------------------

actions/create/genero

actions/list/genero/<int:page>

actions/update/genero/<int:id>

actions/delete/genero/<int:id>

--------------------------------------------------------------------

Para correr el proyecto localmente simplemente usar

### `python manage.py runserver`
