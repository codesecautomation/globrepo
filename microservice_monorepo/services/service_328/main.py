from fastapi import FastAPI

app = FastAPI(title="service_328")

@app.get("/")
def read_root():
    return {"message": "Hello from service_328"}
