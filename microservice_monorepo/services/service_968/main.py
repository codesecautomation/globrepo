from fastapi import FastAPI

app = FastAPI(title="service_968")

@app.get("/")
def read_root():
    return {"message": "Hello from service_968"}
