1. ingresar a la carpeta de trabajo
2. crear un ambiente virtual
    python -m venv drfvenv
3. activar ambiente virtual    
    . drfvenv/Scripts/activate
4. crear el archivo requirements.txt, para instalar lo sgte:
    django
    gunicorn
    django-heroku 
5. instalar el archivo requirements.txt
    pip install -r requirements.txt     
6. crear e inicializr el proyecto
    django-admin startproject hrkmusica .     
8. crear la app
    python manage.py startapp hrkapp
9. agregar hrkapp en el settings (installed_apps)
10. en el settings de hrkmusic colocar lo sgte al final:
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATIC_URL = "/static/"
    django_heroku.settings(locals())   
11. en settings de hrkmusic importar lo sgte:
    import django_heroku
    import os    
12. 
copiar el archvio proclive y cambiar nombre de app de projecto
13. modificar la ruta del gihub si fuera necesario en app.json
    https://github.com/jacquelinebm/PachaQTecMayo2020
14. copiar desde settings el secret key al archivo app.jason
    $!*o_drv7bj3&9bly+v+_6z8x3)s_5t^m(dzzhh@w+2t_%mapf
15. copiar el archvio procfile.windows
16. copiar el archivo runtime.txt
17. verificar que en el settings diga lo sgte:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
18. probar la aplicacion haciendo:
    python manage.py runserver
19.  
                   


