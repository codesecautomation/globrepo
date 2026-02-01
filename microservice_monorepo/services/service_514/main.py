from fastapi import FastAPI

app = FastAPI(title="service_514")

@app.get("/")
def read_root():
    return {"message": "Hello from service_514"}
