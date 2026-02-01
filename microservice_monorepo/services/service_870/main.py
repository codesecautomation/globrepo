from fastapi import FastAPI

app = FastAPI(title="service_870")

@app.get("/")
def read_root():
    return {"message": "Hello from service_870"}
