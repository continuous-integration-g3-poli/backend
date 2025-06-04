# Backend Django Project

Este proyecto es una API backend construida con Django, preparada para desarrollo local y despliegue con Docker.

## Tabla de Contenidos
- [Descripción](#descripción)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Variables de Entorno](#variables-de-entorno)
- [Comandos Útiles](#comandos-útiles)
- [Docker](#docker)
- [Pruebas](#pruebas)
- [Contribución](#contribución)
- [Contacto](#contacto)

## Descripción
API backend basada en Django 5.2.1. Incluye una app de ejemplo llamada `accounts` con endpoint de login.

## Requisitos
- Python 3.11+
- Docker (opcional)

## Instalación
1. Clona el repositorio.
2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```
3. Configura las variables de entorno en un archivo `.env` (ver ejemplo incluido).

## Uso
Para iniciar el servidor de desarrollo:
```bash
python manage.py runserver
```

Accede a la API en `http://localhost:8000/`.

### Endpoint de ejemplo
- `POST /auth/login/` — Login de usuario (ver `accounts/views.py`).

## Estructura del Proyecto
```
backend/
├── accounts/         # App de autenticación
├── core/             # Configuración principal de Django
├── manage.py         # Script de gestión de Django
├── requirements.txt  # Dependencias
├── Dockerfile        # Imagen Docker
├── docker-compose.yml# Orquestación Docker
├── .env              # Variables de entorno
```

## Variables de Entorno
Ejemplo de `.env`:
```
SECRET_KEY=dummy-secret-key
DEBUG=True
```

## Comandos Útiles
- Migraciones:
  ```bash
  python manage.py makemigrations
  python manage.py migrate
  ```
- Crear superusuario:
  ```bash
  python manage.py createsuperuser
  ```

## Docker
Para levantar el entorno con Docker:
```bash
docker-compose up --build
```
La app estará disponible en `http://localhost:8000/`.

## Pruebas
Para ejecutar los tests:
```bash
python manage.py test
```

## Contribución
¡Contribuciones son bienvenidas! Abre un issue o pull request.

## Contacto
Para dudas o soporte, contacta a: [Tu Nombre o Email]