from fastapi import FastAPI

app = FastAPI(title="service_1612")

@app.get("/")
def read_root():
    return {"message": "Hello from service_1612"}
