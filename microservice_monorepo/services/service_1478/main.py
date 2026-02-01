from fastapi import FastAPI

app = FastAPI(title="service_1478")

@app.get("/")
def read_root():
    return {"message": "Hello from service_1478"}
