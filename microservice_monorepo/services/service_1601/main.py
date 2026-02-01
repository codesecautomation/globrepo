from fastapi import FastAPI

app = FastAPI(title="service_1601")

@app.get("/")
def read_root():
    return {"message": "Hello from service_1601"}
