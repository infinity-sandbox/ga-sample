from fastapi import FastAPI
from app.routes.items import router as items_router
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(
    title="My FastAPI App",
    description="A production-grade REST API example",
    version="1.0.0"
)

# Register routes
app.include_router(items_router, prefix="/items", tags=["Items"])

@app.get("/")
def root():
    return {"message": "API is running ✅", "version": "1.0.0"}

@app.get("/health")
def health():
    return {"status": "healthy"}

