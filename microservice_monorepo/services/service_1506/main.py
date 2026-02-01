from fastapi import FastAPI

app = FastAPI(title="service_1506")

@app.get("/")
def read_root():
    return {"message": "Hello from service_1506"}
