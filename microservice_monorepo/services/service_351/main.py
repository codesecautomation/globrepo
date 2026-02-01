from fastapi import FastAPI

app = FastAPI(title="service_351")

@app.get("/")
def read_root():
    return {"message": "Hello from service_351"}
