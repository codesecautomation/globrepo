from fastapi import FastAPI

app = FastAPI(title="service_143")

@app.get("/")
def read_root():
    return {"message": "Hello from service_143"}
