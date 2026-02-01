from fastapi import FastAPI

app = FastAPI(title="service_777")

@app.get("/")
def read_root():
    return {"message": "Hello from service_777"}
