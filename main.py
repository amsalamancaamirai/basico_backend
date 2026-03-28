from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Mi API",
    description="API básica con FastAPI",
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["General"], summary="Hola Mundo")
def hola_mundo():
    """Retorna un saludo de bienvenida."""
    return {"mensaje": "¡Hola, Mundo!"}


@app.get("/saludo/{nombre}", tags=["General"], summary="Saludo personalizado")
def saludo_personalizado(nombre: str):
    """Retorna un saludo personalizado con el nombre proporcionado."""
    return {"mensaje": f"¡Hola, {nombre}!"}
