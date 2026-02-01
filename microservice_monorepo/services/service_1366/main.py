from fastapi import FastAPI

app = FastAPI(title="service_1366")

@app.get("/")
def read_root():
    return {"message": "Hello from service_1366"}
