from fastapi import FastAPI

app = FastAPI(title="service_2108")

@app.get("/")
def read_root():
    return {"message": "Hello from service_2108"}
