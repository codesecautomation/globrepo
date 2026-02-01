from fastapi import FastAPI

app = FastAPI(title="service_4397")

@app.get("/")
def read_root():
    return {"message": "Hello from service_4397"}
