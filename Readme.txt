# 🍋 Little Lemon Restaurant API

[![Django](https://img.shields.io/badge/Django-3.2+-092E20?logo=django)](https://www.djangoproject.com/)
[![DRF](https://img.shields.io/badge/Django_REST_Framework-3.12+-red?logo=django)](https://www.django-rest-framework.org/)
[![MySQL](https://img.shields.io/badge/MySQL-8.0+-4479A1?logo=mysql&logoColor=white)](https://www.mysql.com/)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?logo=python&logoColor=white)](https://www.python.org/)

API RESTful profesional para Little Lemon Restaurant, un restaurante mediterráneo familiar. Proporciona endpoints seguros para gestión de menú, reservaciones y autenticación de usuarios.

## 📋 Tabla de Contenidos

- [Características](#-características)
- [Tecnologías](#️-tecnologías)
- [Requisitos Previos](#-requisitos-previos)
- [Instalación](#-instalación)
- [Configuración](#️-configuración)
- [Uso](#-uso)
- [Endpoints de la API](#-endpoints-de-la-api)
- [Ejemplos de Uso](#-ejemplos-de-uso)
- [Estructura del Proyecto](#-estructura-del-proyecto)
- [Testing](#-testing)
- [Despliegue](#-despliegue)
- [Contribuir](#-contribuir)
- [Licencia](#-licencia)

## ✨ Características

- 🔐 **Autenticación segura** con Token-based authentication
- 👤 **Gestión de usuarios** con registro y login
- 📖 **API de Menú** - CRUD completo para items del menú
- 📅 **API de Reservaciones** - Sistema completo de reservas
- 🛡️ **Permisos y autorizaciones** - Endpoints protegidos
- 📊 **Admin Dashboard** - Panel de administración de Django
- 🔄 **API RESTful** siguiendo mejores prácticas
- 📝 **Serialización de datos** con Django REST Framework
- 💾 **Base de datos MySQL** para producción

## 🛠️ Tecnologías

### Backend
- **Django** - Framework web de Python
- **Django REST Framework (DRF)** - Toolkit para APIs REST
- **Djoser** - Autenticación y gestión de usuarios
- **MySQL** - Sistema de gestión de base de datos

### Paquetes Principales
```
django>=3.2
djangorestframework>=3.12
djoser>=2.1
mysqlclient>=2.0
```

## 📋 Requisitos Previos

Antes de comenzar, asegúrate de tener instalado:

- Python 3.8 o superior
- MySQL 8.0 o superior
- pip (gestor de paquetes de Python)
- Virtualenv (recomendado)

## 📦 Instalación

### 1. Clonar el repositorio

```bash
git clone <url-del-repositorio>
cd AppwebLittleLemon-main
```

### 2. Crear y activar entorno virtual

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/MacOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install django
pip install djangorestframework
pip install djoser
pip install mysqlclient
```

O si tienes un archivo requirements.txt:
```bash
pip install -r requirements.txt
```

### 4. Configurar MySQL

Crea la base de datos en MySQL:

```sql
CREATE DATABASE littlelemon CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'littlelemon_user'@'localhost' IDENTIFIED BY 'tu_contraseña_segura';
GRANT ALL PRIVILEGES ON littlelemon.* TO 'littlelemon_user'@'localhost';
FLUSH PRIVILEGES;
```

## ⚙️ Configuración

### 1. Configurar base de datos

Edita `LittleLemonProject/settings.py` y actualiza la configuración de la base de datos:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'littlelemon',
        'USER': 'littlelemon_user',
        'PASSWORD': 'tu_contraseña_segura',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 2. Variables de entorno (Recomendado)

Crea un archivo `.env` en la raíz del proyecto:

```env
SECRET_KEY=tu-secret-key-super-segura
DEBUG=True
DB_NAME=littlelemon
DB_USER=littlelemon_user
DB_PASSWORD=tu_contraseña_segura
DB_HOST=localhost
DB_PORT=3306
```

### 3. Realizar migraciones

```bash
cd LittleLemonProject
python manage.py makemigrations
python manage.py migrate
```

### 4. Crear superusuario

```bash
python manage.py createsuperuser
```

Sigue las instrucciones para crear tu usuario administrador.

### 5. Iniciar el servidor

```bash
python manage.py runserver
```

La API estará disponible en `http://localhost:8000`

## 🚀 Uso

### Acceder al Admin Dashboard

Visita `http://localhost:8000/admin` e ingresa con las credenciales del superusuario.

### Probar la API

Usa herramientas como:
- **Insomnia** (recomendado)
- **Postman**
- **cURL**
- **HTTPie**

## 📡 Endpoints de la API

### Autenticación

| Método | Endpoint | Descripción | Autenticación |
|--------|----------|-------------|---------------|
| POST | `/auth/users/` | Registrar nuevo usuario | No |
| POST | `/auth/token/login/` | Obtener token de autenticación | No |
| POST | `/auth/token/logout/` | Eliminar token (logout) | Sí |

### Menú

| Método | Endpoint | Descripción | Autenticación |
|--------|----------|-------------|---------------|
| GET | `/api/menu/` | Listar todos los items del menú | Sí |
| POST | `/api/menu/` | Crear nuevo item del menú | Sí |
| GET | `/api/menu/{id}/` | Obtener item específico | Sí |
| PUT | `/api/menu/{id}/` | Actualizar item completo | Sí |
| PATCH | `/api/menu/{id}/` | Actualizar item parcial | Sí |
| DELETE | `/api/menu/{id}/` | Eliminar item | Sí |

### Reservaciones

| Método | Endpoint | Descripción | Autenticación |
|--------|----------|-------------|---------------|
| GET | `/api/bookings/` | Listar todas las reservaciones | Sí |
| POST | `/api/bookings/` | Crear nueva reservación | Sí |
| GET | `/api/bookings/{id}/` | Obtener reservación específica | Sí |
| PUT | `/api/bookings/{id}/` | Actualizar reservación completa | Sí |
| PATCH | `/api/bookings/{id}/` | Actualizar reservación parcial | Sí |
| DELETE | `/api/bookings/{id}/` | Eliminar reservación | Sí |

## 💡 Ejemplos de Uso

### 1. Registrar un nuevo usuario

```bash
curl -X POST http://localhost:8000/auth/users/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "johndoe",
    "password": "securepassword123",
    "email": "john@example.com"
  }'
```

**Respuesta:**
```json
{
  "email": "john@example.com",
  "username": "johndoe",
  "id": 1
}
```

### 2. Obtener token de autenticación

```bash
curl -X POST http://localhost:8000/auth/token/login/ \
  -H "Content-Type: application/json" \
  -d '{
    "username": "johndoe",
    "password": "securepassword123"
  }'
```

**Respuesta:**
```json
{
  "auth_token": "9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"
}
```

### 3. Crear un item del menú

```bash
curl -X POST http://localhost:8000/api/menu/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b" \
  -d '{
    "title": "Greek Salad",
    "price": "12.99",
    "inventory": 50
  }'
```

**Respuesta:**
```json
{
  "id": 1,
  "title": "Greek Salad",
  "price": "12.99",
  "inventory": 50
}
```

### 4. Listar items del menú

```bash
curl -X GET http://localhost:8000/api/menu/ \
  -H "Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"
```

### 5. Crear una reservación

```bash
curl -X POST http://localhost:8000/api/bookings/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b" \
  -d '{
    "name": "John Doe",
    "no_of_guests": 4,
    "booking_date": "2026-02-15T19:00:00Z"
  }'
```

**Respuesta:**
```json
{
  "id": 1,
  "user": 1,
  "name": "John Doe",
  "no_of_guests": 4,
  "booking_date": "2026-02-15T19:00:00Z"
}
```

### 6. Actualizar una reservación (PATCH)

```bash
curl -X PATCH http://localhost:8000/api/bookings/1/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b" \
  -d '{
    "no_of_guests": 6
  }'
```

### 7. Eliminar un item del menú

```bash
curl -X DELETE http://localhost:8000/api/menu/1/ \
  -H "Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"
```

### 8. Cerrar sesión (Logout)

```bash
curl -X POST http://localhost:8000/auth/token/logout/ \
  -H "Authorization: Token 9944b09199c62bcf9418ad846dd0e4bbdfc6ee4b"
```

## 📁 Estructura del Proyecto

```
AppwebLittleLemon-main/
└── LittleLemonProject/
    ├── LittleLemonProject/          # Configuración del proyecto
    │   ├── __init__.py
    │   ├── settings.py              # Configuración principal
    │   ├── urls.py                  # URLs principales
    │   ├── asgi.py                  # Configuración ASGI
    │   └── wsgi.py                  # Configuración WSGI
    │
    ├── LittleLemonAPI/              # Aplicación principal
    │   ├── __init__.py
    │   ├── models.py                # Modelos (Menu, Booking)
    │   ├── serializers.py           # Serializers DRF
    │   ├── views.py                 # Vistas de la API
    │   ├── urls.py                  # URLs de la API
    │   ├── admin.py                 # Configuración del admin
    │   ├── apps.py                  # Configuración de la app
    │   └── tests.py                 # Tests unitarios
    │
    └── manage.py                    # Script de gestión Django
```

## 📊 Modelos de Datos

### Menu Model

```python
class Menu(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
```

**Campos:**
- `id` (AutoField): ID único del item
- `title` (CharField): Nombre del plato
- `price` (DecimalField): Precio del plato
- `inventory` (IntegerField): Cantidad en inventario

### Booking Model

```python
class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField()
    booking_date = models.DateTimeField()
```

**Campos:**
- `id` (AutoField): ID único de la reservación
- `user` (ForeignKey): Usuario que hizo la reservación
- `name` (CharField): Nombre para la reservación
- `no_of_guests` (IntegerField): Número de invitados
- `booking_date` (DateTimeField): Fecha y hora de la reservación

## 🧪 Testing

### Ejecutar tests

```bash
python manage.py test
```

### Ejecutar tests con cobertura

```bash
pip install coverage
coverage run --source='.' manage.py test
coverage report
coverage html  # Genera reporte HTML
```

### Ejemplo de test

```python
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User

class MenuAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.client.force_authenticate(user=self.user)
    
    def test_get_menu_list(self):
        response = self.client.get('/api/menu/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
```

## 🐛 Solución de Problemas

### Error de conexión a MySQL

```bash
# Verifica que MySQL esté corriendo
sudo systemctl status mysql  # Linux
# o
brew services list           # MacOS

# Verifica las credenciales
mysql -u littlelemon_user -p
```

### Error de migraciones

```bash
# Resetear migraciones
python manage.py migrate --run-syncdb
```

### Token inválido

El token puede expirar. Obtén uno nuevo con el endpoint `/auth/token/login/`

### Problemas con mysqlclient

**Windows:**
```bash
pip install mysqlclient
# Si falla, instala desde wheel:
pip install https://download.lfd.uci.edu/pythonlibs/archived/mysqlclient-2.1.1-cp39-cp39-win_amd64.whl
```

**Linux:**
```bash
sudo apt-get install python3-dev default-libmysqlclient-dev build-essential
pip install mysqlclient
```

## 🚀 Despliegue

### Preparación para producción

1. **Actualizar settings.py:**

```python
DEBUG = False
ALLOWED_HOSTS = ['tudominio.com', 'www.tudominio.com']

# Configuración de seguridad
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
```

2. **Recolectar archivos estáticos:**

```bash
python manage.py collectstatic
```

3. **Usar variables de entorno:**

```bash
pip install python-decouple
```

### Opciones de despliegue

- **Heroku** - Plataforma PaaS fácil de usar
- **AWS EC2** - Servidor virtual en la nube
- **DigitalOcean** - VPS sencillo y económico
- **Google Cloud Platform** - Infraestructura escalable
- **Railway** - Plataforma moderna para Django

## 🔒 Seguridad

### Mejores prácticas implementadas

- ✅ Autenticación basada en tokens
- ✅ Permisos por endpoint
- ✅ Validación de datos con serializers
- ✅ Protección CSRF
- ✅ SQL injection prevention (ORM)

### Recomendaciones adicionales

- Usa HTTPS en producción
- Configura rate limiting
- Implementa logging
- Mantén dependencias actualizadas
- Usa variables de entorno para secretos

## 📚 Recursos Adicionales

- [Documentación de Django](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Djoser Documentation](https://djoser.readthedocs.io/)
- [MySQL Documentation](https://dev.mysql.com/doc/)

## 🤝 Contribuir

Las contribuciones son bienvenidas. Para cambios importantes:

1. Fork el proyecto
2. Crea una rama (`git checkout -b feature/NuevaCaracteristica`)
3. Commit tus cambios (`git commit -m 'Agregar nueva característica'`)
4. Push a la rama (`git push origin feature/NuevaCaracteristica`)
5. Abre un Pull Request

### Guías de contribución

- Sigue PEP 8 para estilo de código Python
- Escribe tests para nuevas funcionalidades
- Actualiza la documentación según sea necesario
- Mantén los commits claros y descriptivos

## 📝 Changelog

### [1.0.0] - 2025

#### Agregado
- API de autenticación con Djoser
- CRUD completo para menú
- CRUD completo para reservaciones
- Token authentication
- Admin dashboard

## 📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## 👥 Autores

- Andres Felipe Celi Jimenez para el Curso de Meta

## 🙏 Agradecimientos

- Meta/Facebook por el capstone project
- Comunidad de Django y DRF
- Todos los contribuidores del proyecto

---

*Este proyecto fue desarrollado como parte del Meta Back-End Developer Professional Certificate.*
