from fastapi import FastAPI

app = FastAPI(title="service_087")

@app.get("/")
def read_root():
    return {"message": "Hello from service_087"}
