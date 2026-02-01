from fastapi import FastAPI

app = FastAPI(title="service_5000")

@app.get("/")
def read_root():
    return {"message": "Hello from service_5000"}
