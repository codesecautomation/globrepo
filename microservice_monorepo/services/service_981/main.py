from fastapi import FastAPI

app = FastAPI(title="service_981")

@app.get("/")
def read_root():
    return {"message": "Hello from service_981"}
