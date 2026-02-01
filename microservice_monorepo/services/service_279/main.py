from fastapi import FastAPI

app = FastAPI(title="service_279")

@app.get("/")
def read_root():
    return {"message": "Hello from service_279"}
