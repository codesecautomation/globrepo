from fastapi import FastAPI

app = FastAPI(title="service_306")

@app.get("/")
def read_root():
    return {"message": "Hello from service_306"}
