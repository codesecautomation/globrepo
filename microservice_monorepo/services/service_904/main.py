from fastapi import FastAPI

app = FastAPI(title="service_904")

@app.get("/")
def read_root():
    return {"message": "Hello from service_904"}
