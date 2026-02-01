from fastapi import FastAPI

app = FastAPI(title="service_1853")

@app.get("/")
def read_root():
    return {"message": "Hello from service_1853"}
