from fastapi import FastAPI

app = FastAPI(title="service_801")

@app.get("/")
def read_root():
    return {"message": "Hello from service_801"}
