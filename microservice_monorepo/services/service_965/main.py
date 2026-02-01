from fastapi import FastAPI

app = FastAPI(title="service_965")

@app.get("/")
def read_root():
    return {"message": "Hello from service_965"}
