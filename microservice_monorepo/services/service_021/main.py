from fastapi import FastAPI

app = FastAPI(title="service_021")

@app.get("/")
def read_root():
    return {"message": "Hello from service_021"}
