# CRUD_Usuarios
![Django Logo](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)![Tailwind Logo](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)

Esta aplicación permite crear, leer, actualizar y eliminar usuarios de forma rápida y sencilla

## Requisitos

Sigue estos pasos para instalar y configurar la aplicación en tu entorno local.

### Copiar el repositorio y configurar entorno virtual
```
git clone https://github.com/jeffrmdev/crud_usuarios.git
cd <ruta_del_proyecto>
pip install pipenv
pipenv --venv
```

### Instalar dependencias

```
pip install -r requirements.txt
```
### Aplicar migraciones y creación del usuario

```
python manage.py migrate
python manage.py createsuperuser #opcional
```

## Ejecutar la aplicacion
```
python manage.py runserver
``` 

Si todo salió bien, la aplicación se ejecutará en la siguiente dirección:
http://127.0.0.1:8000/



### Requisitos Previos

Instalar git desde:  
https://git-scm.com/downloads  
Instalar python 3.12 en tu ordenador desde:  
https://www.python.org/downloads/

Seleccionar el instalador según el sistema operativo

