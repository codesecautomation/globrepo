from fastapi import FastAPI

app = FastAPI(title="service_220")

@app.get("/")
def read_root():
    return {"message": "Hello from service_220"}
