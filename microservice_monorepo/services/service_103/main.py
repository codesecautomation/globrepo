from fastapi import FastAPI

app = FastAPI(title="service_103")

@app.get("/")
def read_root():
    return {"message": "Hello from service_103"}
