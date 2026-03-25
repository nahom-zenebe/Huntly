from fastapi import FastAPI


app = FastAPI(
    title="Huntly API",
    description="API for Huntly application",
    version="1.0.0",
)


@app.get("/")
def main():
    return {"message": "Hello World"}