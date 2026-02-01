from fastapi import FastAPI

app = FastAPI(title="service_144")

@app.get("/")
def read_root():
    return {"message": "Hello from service_144"}
