from fastapi import FastAPI

app = FastAPI(title="service_861")

@app.get("/")
def read_root():
    return {"message": "Hello from service_861"}
