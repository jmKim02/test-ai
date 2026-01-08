# main.py
from fastapi import FastAPI

app = FastAPI(
    title="AI Server",
    description="FastAPI 배포 테스트",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "AI Server is running! 🚀",
        "status": "OK"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "ai-server"
    }

@app.get("/api/predict")
def predict():
    return {
        "result": "This is a dummy prediction",
        "confidence": 0.95
    }