from fastapi import FastAPI

app = FastAPI(title="service_1860")

@app.get("/")
def read_root():
    return {"message": "Hello from service_1860"}
