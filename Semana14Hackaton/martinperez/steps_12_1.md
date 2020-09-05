1. Ir a la carpeta de trabajo
2. Crear ambiente virtual
    python -m venv djenv
3. Activar ambiente virtual
    . djenv/Scripts/activate
4. Instalar dependencias
    pip install django
    pip install psycopg2
5. Inicializamos el proyecto
    django-admin startproject whtsppPedidos
6. Inicializamos la aplicacion django
    python manage.py startapp whtspp
    python manage.py startapp mssngr
    python manage.py startapp tlgrm
    python manage.py startapp pdds
    python manage.py startapp lndng

6. 1. Configurar base de datos Postgres
    socialpedidos


7. Modificamos los settings.py para usar postgres
    LANGUAGE_CODE = 'es-us'
    TIME_ZONE = 'America/Lima'
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'socialpedidos',
            'USER': 'postgres',
            'PASSWORD': 'passmysqlmartin',
            'HOST': '127.0.0.1',
            'PORT': '5432',
        }
    }
    INSTALLED_APPS = [
        'whtspp.apps.WhtsppConfig',
        'tlgrm.apps.TlgrmConfig',
        'pdds.apps.PddsConfig',
        'mssngr.apps.MssngrConfig',
    ]
 
8. Ejecutamos las migracions de django
    python manage.py migrate
   Ejecutar aplicacion y arrancar pagina:
    python manage.py runserver


8. 1. crear super usuario
    python manage.py createsuperuser

9. Registrar aplicaciones en admin de django
    

10. Creamos super usuario 
    python manage.py createsuperuser

11. Creamos los models

11. 1.  ver todos los comandos ejecutados:
        history  

12. Inicializamos las migraciones
    python  manage.py makemigrations
13. Ejecutamos las migraciones
    python manage.py migrate
    python manage.py migrate:refresh

14. Instalamos django-adminlte
14. 1. AGREGAR REFERENCIAS
    # General use templates & template tags (should appear first)
    'adminlte3',
     # Optional: Django admin theme (must be before django.contrib.admin)
    'adminlte3_theme',

14. 2. INSTALAR:
    pip install django-adminlte3
15. Instalar el collctstics
15. 1. PONER 
        import os
        # Static files (CSS, JavaScript, Images)
        # https://docs.djangoproject.com/en/3.1/howto/static-files/
        PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))
        STATIC_ROOT = os.path.join(PROJECT_DIR, 'static')
        STATIC_URL = '/static/'

15. 2. Instalar el collctstics
    python manage.py collectstatic

16. instalar sweetalert2
    "{% static '/js/sweetalert2.js'%}"
    "{% static '/css/sweetalert2.css'%}"


17. instalar el autopep8, correcciones de estructura de escritura
    pip install autopep8


18. pasar a requirements
    pip freeze > requirements.txt

19. para messenger Facebook.. instalar el requests
    pip install requests

