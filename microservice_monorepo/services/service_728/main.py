from fastapi import FastAPI

app = FastAPI(title="service_728")

@app.get("/")
def read_root():
    return {"message": "Hello from service_728"}
