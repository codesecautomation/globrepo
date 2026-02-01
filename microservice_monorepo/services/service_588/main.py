from fastapi import FastAPI

app = FastAPI(title="service_588")

@app.get("/")
def read_root():
    return {"message": "Hello from service_588"}
