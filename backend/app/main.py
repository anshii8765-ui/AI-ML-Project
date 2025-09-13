from fastapi import FastAPI
from .database import Base, engine
from . import models
from .routers import users, medicines, prescriptions

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="MediRead Backend", version="0.1.0")

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(users.router)
app.include_router(medicines.router)
app.include_router(prescriptions.router)

