from fastapi import FastAPI

app = FastAPI(title="service_3861")

@app.get("/")
def read_root():
    return {"message": "Hello from service_3861"}
