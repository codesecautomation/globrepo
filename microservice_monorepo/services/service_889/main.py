from fastapi import FastAPI

app = FastAPI(title="service_889")

@app.get("/")
def read_root():
    return {"message": "Hello from service_889"}
