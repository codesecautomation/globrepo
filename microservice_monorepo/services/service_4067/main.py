from fastapi import FastAPI

app = FastAPI(title="service_4067")

@app.get("/")
def read_root():
    return {"message": "Hello from service_4067"}
