from fastapi import FastAPI

app = FastAPI(title="service_954")

@app.get("/")
def read_root():
    return {"message": "Hello from service_954"}
