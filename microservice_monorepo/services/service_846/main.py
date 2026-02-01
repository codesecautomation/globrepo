from fastapi import FastAPI

app = FastAPI(title="service_846")

@app.get("/")
def read_root():
    return {"message": "Hello from service_846"}
