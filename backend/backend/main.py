from fastapi import FastAPI
from backend.routes import klebsiela
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    'http://localhost:8000',
    'http://localhost:8001',
    'http://localhost:8081',
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(klebsiela.router)