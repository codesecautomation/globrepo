from fastapi import FastAPI

app = FastAPI(title="service_1791")

@app.get("/")
def read_root():
    return {"message": "Hello from service_1791"}
