# Inicio

Para poder utilizar este programa por primera vez, debe ejecutar los siguientes comandos en la carpeta donde se encuentre el archivo manage.py, es necesario tener Python 3.13 o superior:

```
  python manage.py makemigrations
  python manage.py migrate
  python manage.py createsuperuser
```

Tras ejecutar el ultimo comando deberá crear un super usuario. Por ultimo puede correr el servidor para comenzar a utilizar el programa:

```
  python manage.py runserver
```

Si ahora entra a la dirección del servidor desde el navegador web y se dirije a /admin, podrá iniciar sesion con su super usuario y hacer uso del programa.
