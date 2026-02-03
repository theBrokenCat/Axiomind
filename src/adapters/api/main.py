from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config.settings import settings
from config.logging import setup_logging
from src.adapters.api.v1.router import api_router
from src.adapters.api.auth_middleware import AuthMiddleware

# Setup logging
setup_logging()

app = FastAPI(
    title=settings.API_TITLE,
    version=settings.API_VERSION
)

# Integración de Sentinel (The Doorkeeper)
app.add_middleware(AuthMiddleware)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include Routers
app.include_router(api_router, prefix="/api/v1", tags=["v1"])

@app.get("/health")
async def health_check():
    return {"status": "ok", "version": settings.API_VERSION}

@app.on_event("startup")
async def startup_event():
    # Potential database connection initialization
    pass

@app.on_event("shutdown")
async def shutdown_event():
    # Potential cleanup
    pass
