from fastapi import FastAPI

app = FastAPI(title="service_270")

@app.get("/")
def read_root():
    return {"message": "Hello from service_270"}
