from fastapi import FastAPI

app = FastAPI(title="service_108")

@app.get("/")
def read_root():
    return {"message": "Hello from service_108"}
