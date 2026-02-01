from fastapi import FastAPI

app = FastAPI(title="service_703")

@app.get("/")
def read_root():
    return {"message": "Hello from service_703"}
