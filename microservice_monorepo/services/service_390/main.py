from fastapi import FastAPI

app = FastAPI(title="service_390")

@app.get("/")
def read_root():
    return {"message": "Hello from service_390"}
