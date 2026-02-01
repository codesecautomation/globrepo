from fastapi import FastAPI

app = FastAPI(title="service_707")

@app.get("/")
def read_root():
    return {"message": "Hello from service_707"}
