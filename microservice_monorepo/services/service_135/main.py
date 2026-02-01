from fastapi import FastAPI

app = FastAPI(title="service_135")

@app.get("/")
def read_root():
    return {"message": "Hello from service_135"}
