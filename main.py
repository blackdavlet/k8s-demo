from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok", "message": "running in kubernetes"}

@app.get("/health")
def health():
    return {"healthy": True}