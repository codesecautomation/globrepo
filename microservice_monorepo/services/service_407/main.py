from fastapi import FastAPI

app = FastAPI(title="service_407")

@app.get("/")
def read_root():
    return {"message": "Hello from service_407"}
