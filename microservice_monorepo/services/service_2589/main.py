from fastapi import FastAPI

app = FastAPI(title="service_2589")

@app.get("/")
def read_root():
    return {"message": "Hello from service_2589"}
