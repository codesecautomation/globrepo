from fastapi import FastAPI

app = FastAPI(title="service_4853")

@app.get("/")
def read_root():
    return {"message": "Hello from service_4853"}
