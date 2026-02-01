from fastapi import FastAPI

app = FastAPI(title="service_1703")

@app.get("/")
def read_root():
    return {"message": "Hello from service_1703"}
