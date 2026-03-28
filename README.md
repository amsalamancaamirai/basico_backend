# 🚀 Basico Backend — FastAPI

API básica construida con **FastAPI** que incluye documentación automática con Swagger.

---

## 📋 Requisitos

- Python 3.10+
- pip

---

## ⚙️ Ejecución local

### 1. Clona el repositorio

```bash
git clone https://github.com/amsalamancaamirai/basico_backend.git
cd basico_backend
```

### 2. Crea y activa un entorno virtual

```bash
# Crear entorno virtual
python -m venv venv

# Activar en Linux/Mac
source venv/bin/activate

# Activar en Windows
venv\Scripts\activate
```

### 3. Instala las dependencias

```bash
pip install fastapi uvicorn
```

### 4. Levanta el servidor

```bash
uvicorn main:app --reload
```

### 5. Accede a la API

| URL | Descripción |
|-----|-------------|
| `http://localhost:8000/` | Hola Mundo |
| `http://localhost:8000/saludo/{nombre}` | Saludo personalizado |
| `http://localhost:8000/docs` | Swagger UI |
| `http://localhost:8000/redoc` | ReDoc |

---

## 🐳 Despliegue con Docker

### Requisitos

- [Docker](https://www.docker.com/get-started) instalado

### 1. Construye la imagen

```bash
docker build -t basico-backend .
```

### 2. Corre el contenedor

```bash
docker run -d -p 8000:8000 --name basico-backend basico-backend
```

### 3. Accede a la API

Mismas URLs que en ejecución local:
- Swagger: `http://localhost:8000/docs`

### Comandos útiles de Docker

```bash
# Ver logs del contenedor
docker logs basico-backend

# Detener el contenedor
docker stop basico-backend

# Eliminar el contenedor
docker rm basico-backend

# Eliminar la imagen
docker rmi basico-backend
```

---

## 📦 Docker Compose (opcional)

Si prefieres usar Docker Compose:

```bash
docker compose up -d
```

Para detenerlo:

```bash
docker compose down
```

---

## 📁 Estructura del proyecto

```
basico_backend/
├── main.py            # Aplicación FastAPI
├── Dockerfile         # Imagen Docker
├── docker-compose.yml # Compose opcional
└── README.md          # Este archivo
```
