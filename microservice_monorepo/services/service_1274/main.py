from fastapi import FastAPI

app = FastAPI(title="service_1274")

@app.get("/")
def read_root():
    return {"message": "Hello from service_1274"}
