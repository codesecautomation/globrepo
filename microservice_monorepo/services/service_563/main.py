from fastapi import FastAPI

app = FastAPI(title="service_563")

@app.get("/")
def read_root():
    return {"message": "Hello from service_563"}
