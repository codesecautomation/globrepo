from fastapi import FastAPI

app = FastAPI(title="service_2380")

@app.get("/")
def read_root():
    return {"message": "Hello from service_2380"}
