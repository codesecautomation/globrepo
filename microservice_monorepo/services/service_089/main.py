from fastapi import FastAPI

app = FastAPI(title="service_089")

@app.get("/")
def read_root():
    return {"message": "Hello from service_089"}
