from fastapi import FastAPI

app = FastAPI(title="service_1700")

@app.get("/")
def read_root():
    return {"message": "Hello from service_1700"}
