from fastapi import FastAPI

app = FastAPI(title="service_177")

@app.get("/")
def read_root():
    return {"message": "Hello from service_177"}
