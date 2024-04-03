import sys
sys.path.append(".")

from fastapi import FastAPI
from app.routers import events
from app.config import Base, engine


Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Gestión de Eventos",
    description="API para gestionar eventos de una empresa de café",
    version="1.0.0"
)

app.include_router(events.router)

@app.get("/")
def read_root():
    return {"message": "Bienvenido a la API de Gestión de Eventos"}