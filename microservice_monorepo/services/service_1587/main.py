from fastapi import FastAPI

app = FastAPI(title="service_1587")

@app.get("/")
def read_root():
    return {"message": "Hello from service_1587"}
