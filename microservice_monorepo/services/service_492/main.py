from fastapi import FastAPI

app = FastAPI(title="service_492")

@app.get("/")
def read_root():
    return {"message": "Hello from service_492"}
