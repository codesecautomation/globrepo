from fastapi import FastAPI

app = FastAPI(title="service_4500")

@app.get("/")
def read_root():
    return {"message": "Hello from service_4500"}
