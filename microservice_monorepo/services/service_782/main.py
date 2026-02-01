from fastapi import FastAPI

app = FastAPI(title="service_782")

@app.get("/")
def read_root():
    return {"message": "Hello from service_782"}
