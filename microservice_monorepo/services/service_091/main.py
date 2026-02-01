from fastapi import FastAPI

app = FastAPI(title="service_091")

@app.get("/")
def read_root():
    return {"message": "Hello from service_091"}
