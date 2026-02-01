from fastapi import FastAPI

app = FastAPI(title="service_1080")

@app.get("/")
def read_root():
    return {"message": "Hello from service_1080"}
