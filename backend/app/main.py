from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import PROJECT_NAME, API_VERSION, DESCRIPTION

app = FastAPI(
    title=PROJECT_NAME,
    version=API_VERSION,
    description=DESCRIPTION
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "message": "Welcome to TerraSpectra API"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "project": "TerraSpectra"
    }