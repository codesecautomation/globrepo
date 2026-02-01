from fastapi import FastAPI

app = FastAPI(title="service_2436")

@app.get("/")
def read_root():
    return {"message": "Hello from service_2436"}
