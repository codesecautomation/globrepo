from fastapi import FastAPI

app = FastAPI(title="service_1756")

@app.get("/")
def read_root():
    return {"message": "Hello from service_1756"}
