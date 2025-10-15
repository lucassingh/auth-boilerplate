## 🧠 **EXPLICACIÓN DEL CÓDIGO - Cómo funciona todo**

### **🏗️ ARQUITECTURA DEL PROYECTO**

CLIENTE (Frontend/Postman)
↓
FASTAPI (app/main.py) ←→ SWAGGER DOCS
↓
ENDPOINTS (app/api/) → SCHEMAS (app/schemas/)
↓
SERVICIOS (app/services/) → CRUD (app/crud/)
↓
MODELOS (app/models/) ←→ BASE DE DATOS (PostgreSQL)
↓
CONFIGURACIÓN (app/core/)

### **🔧 COMPONENTES PRINCIPALES:**

#### **1. 🐳 DOCKER-COMPOSE.YML** - "El Orquestador"
```yaml
services:
  web:    # Tu aplicación FastAPI (construida desde Dockerfile)
  db:     # PostgreSQL (imagen pre-hecha)
  pgadmin: # Interfaz web para la base de datos

### FunciÓn: Levanta 3 servicios que se comunican entre sí.

### 2. 🐋 DOCKERFILE - "La Receta"

FROM python:3.11-slim  # Imagen base
WORKDIR /app           # Directorio de trabajo
COPY . .              # Copia tu código
RUN pip install...    # Instala dependencias
CMD ["uvicorn..."]    # Comando para ejecutar

### FunciÓn: Crea una imagen con tu aplicación lista para ejecutar.

### 3. ⚙️ APP/CORE/CONFIG.PY - "Las Configuraciones"

class Settings(BaseSettings):
    SECRET_KEY: str      # Para JWT tokens
    DATABASE_URL: str    # Conexión a PostgreSQL
    # ... más configs

### FunciÓn: Centraliza todas las configuraciones desde variables de entorno.

### 4. 🗄️ APP/MODELS/ - "La Estructura de Datos"

python
class User(BaseModel):
    email: str
    hashed_password: str
    # ... más campos

### FunciÓn: Define cómo se ven las tablas en la base de datos.

### 5. 📝 APP/SCHEMAS/ - "Los Contratos de la API"

python
class UserCreate(BaseModel):
    email: EmailStr      # Validación automática
    password: str
    # ... más campos

### FunciÓn: Define qué datos espera/retorna la API con validación.

### 🔄 FLUJO DE UNA PETICIÓN:

Cliente → POST /api/v1/auth/login con email/password

FastAPI → Valida datos con LoginRequest schema

Endpoint → Llama a AuthService.authenticate()

Servicio → Usa CRUDUser.authenticate()

CRUD → Consulta la base de datos con SQLAlchemy

Modelo → User table en PostgreSQL

Respuesta ← Token JWT generado con SecurityService

### 🔐 SISTEMA DE AUTENTICACIÓN:

python
# Login: email/password → JWT Token
# Registro: datos usuario → Usuario en DB + Email verificación
# JWT Token → Acceso a endpoints protegidos
# Refresh Token → Renovar JWT expirado
# Password Reset → Email con código/token

### 📊 BASE DE DATOS - TABLAS PRINCIPALES:

users: Usuarios del sistema

refresh_tokens: Tokens para renovar JWT

password_reset_codes: Códigos para resetear contraseña

## 📁 ESTRUCTURA DEL PROYECTO

auth-boilerplate/
├── 🐳 docker-compose.yml    # Orquestador de servicios
├── 🐋 Dockerfile            # Imagen de la aplicación
├── 📋 requirements.txt      # Dependencias Python
├── 🔧 .env                  # Variables de entorno
├── 📊 create_tables.py      # Script creación tablas
├── 🔍 check_tables.py       # Script verificación
└── 📁 app/
    ├── 🏠 main.py           # Aplicación FastAPI principal
    ├── ⚙️ core/             # Configuración y utilidades
    ├── 🗄️ models/          # Modelos de base de datos
    ├── 📝 schemas/          # Esquemas Pydantic
    ├── 🛠️ crud/            # Operaciones de base de datos
    ├── 🚀 api/              # Endpoints de la API
    ├── 📧 services/         # Lógica de negocio
    └── 🧪 tests/            # Tests automatizados

# 🐳 Comandos Auth Boilerplate

## 🚀 INICIAR PROYECTO CON DOCKER
```bash
# Levantar todos los servicios
docker-compose up -d

# Levantar y reconstruir imágenes
docker-compose up -d --build

# Ver estado de contenedores
docker-compose ps

# Ver logs en tiempo real
docker-compose logs -f

# Detener contenedores
docker-compose down

## ⏹️ DETENER PROYECTO

# Detener y eliminar volúmenes (CUIDADO: borra datos)
docker-compose down -v

## 🔧 DESARROLLO

# Ejecutar comandos dentro del contenedor web
docker-compose exec web [comando]

# Ejemplos:
docker-compose exec web python create_tables.py
docker-compose exec web python check_tables.py
docker-compose exec web alembic upgrade head

# Acceder a shell del contenedor
docker-compose exec web bash

# Ver logs específicos
docker-compose logs web
docker-compose logs db

## 🗄️ BASE DE DATOS

# Conectar a PostgreSQL directamente
docker-compose exec db psql -U postgres -d auth_boilerplate

# Ver tablas
docker-compose exec db psql -U postgres -d auth_boilerplate -c "\dt"

# Verificar que PostgreSQL esté listo
docker-compose exec db pg_isready

## 🎯 URLS DE ACCESO

API: http://localhost:8000

Swagger UI: http://localhost:8000/docs

Redoc: http://localhost:8000/redoc

pgAdmin: http://localhost:8080 (admin@admin.com / admin)

##  🔍 TROUBLESHOOTING

# Reconstruir forzadamente
docker-compose build --no-cache

# Ver uso de recursos
docker-compose stats

# Limpiar Docker
docker system prune

## 🐍 Comandos Python - Desarrollo Local

# Crear y activar entorno virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar aplicación
uvicorn app.main:app --reload

## 🧪 DESARROLLO

# Crear tablas
python create_tables.py

# Verificar tablas
python check_tables.py

# Ejecutar tests
pytest

# Formatear código
black app/
isort app/

📊 BASE DE DATOS

# Migraciones con Alembic
alembic revision --autogenerate -m "descripción"
alembic upgrade head
alembic downgrade -1

## 🚀 ENDPOINTS

# Registrar usuario
curl -X POST "http://localhost:8000/api/v1/auth/register" \
  -H "Content-Type: application/json" \
  -d '{"email":"user@example.com","password":"password123","first_name":"John","last_name":"Doe"}'

# Login
curl -X POST "http://localhost:8000/api/v1/auth/login" \
  -H "Content-Type: application/json" \
  -d '{"email":"user@example.com","password":"password123"}'

# Ver perfil (con token)
curl -X GET "http://localhost:8000/api/v1/users/me" \
  -H "Authorization: Bearer [TOKEN]"

## 🔐 ADMIN

# Health check
curl http://localhost:8000/health

# Ver documentación interactiva
# Navegar a: http://localhost:8000/docs


