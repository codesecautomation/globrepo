from fastapi import FastAPI

app = FastAPI(title="service_486")

@app.get("/")
def read_root():
    return {"message": "Hello from service_486"}
