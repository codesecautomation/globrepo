from fastapi import FastAPI

app = FastAPI(title="service_1944")

@app.get("/")
def read_root():
    return {"message": "Hello from service_1944"}
