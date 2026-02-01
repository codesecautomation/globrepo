from fastapi import FastAPI

app = FastAPI(title="service_1731")

@app.get("/")
def read_root():
    return {"message": "Hello from service_1731"}
