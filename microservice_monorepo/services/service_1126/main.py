from fastapi import FastAPI

app = FastAPI(title="service_1126")

@app.get("/")
def read_root():
    return {"message": "Hello from service_1126"}
