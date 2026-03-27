from fastapi import FastAPI
from app.tasks.scheduler import start_scheduler

app = FastAPI(
    title="Huntly API",
    description="API for Huntly application",
    version="1.0.0",
)


@app.on_event("startup")
def startup_event():
    start_scheduler()
    

@app.get("/")
def main():
    return {"message": "Hello World"}