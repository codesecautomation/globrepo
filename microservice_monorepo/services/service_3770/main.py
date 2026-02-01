from fastapi import FastAPI

app = FastAPI(title="service_3770")

@app.get("/")
def read_root():
    return {"message": "Hello from service_3770"}
