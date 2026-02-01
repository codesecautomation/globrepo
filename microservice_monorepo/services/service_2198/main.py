from fastapi import FastAPI

app = FastAPI(title="service_2198")

@app.get("/")
def read_root():
    return {"message": "Hello from service_2198"}
