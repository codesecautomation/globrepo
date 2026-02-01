from fastapi import FastAPI

app = FastAPI(title="service_196")

@app.get("/")
def read_root():
    return {"message": "Hello from service_196"}
