from fastapi import FastAPI

app = FastAPI(title="service_3781")

@app.get("/")
def read_root():
    return {"message": "Hello from service_3781"}
