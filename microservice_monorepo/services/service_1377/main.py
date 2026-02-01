from fastapi import FastAPI

app = FastAPI(title="service_1377")

@app.get("/")
def read_root():
    return {"message": "Hello from service_1377"}
