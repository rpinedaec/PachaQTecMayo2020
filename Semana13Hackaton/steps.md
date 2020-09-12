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
    python manage.py startapp authenticate

7. Modificamos los settings.py para usar postgres

8. Ejecutamos las migracions de django
    python manage.py migrate

9. Registrar aplicaciones en admin de django

10. Creamos super usuario 
    python manage.py createsuperuser

11. Creamos los models

12. Inicializamos las migraciones
    python manage.py makemigrations
13. Ejecutamos las migraciones
    python manage.py migrate
14. Instalamos django-adminlte3
    pip install django-adminlte3
15. Instalar el collctstics
    python manage.py collectstatic

16. agregar forms.py en la aplicacion authenticate

17. modificacion de urls
