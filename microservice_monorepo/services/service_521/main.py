from fastapi import FastAPI

app = FastAPI(title="service_521")

@app.get("/")
def read_root():
    return {"message": "Hello from service_521"}
