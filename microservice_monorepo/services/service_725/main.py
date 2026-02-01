from fastapi import FastAPI

app = FastAPI(title="service_725")

@app.get("/")
def read_root():
    return {"message": "Hello from service_725"}
