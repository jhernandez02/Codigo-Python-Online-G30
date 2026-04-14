# Introducción a Django

## Instalación

```bash
python -m venv entorno_django
source entorno_django/Scripts/activate
pip install django
```

## Creación del proyecto

```bash
django-admin startproject django_intro .
```

## Inicio del servidor

```bash
python manage.py runserver
```

## Migraciones

```bash
# Crear los documentos de migraciones
python manage.py makemigrations

# Ejecutar las migraciones
python manage.py migrate

# Listar las migraciones
python manage.py showmigrations
```

## Creación de usuario

```bash
python manage.py createsuperuser
```

## Creación de aplicación

```bash
python manage.py startapp almacen
```