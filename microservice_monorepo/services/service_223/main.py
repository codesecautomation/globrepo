from fastapi import FastAPI

app = FastAPI(title="service_223")

@app.get("/")
def read_root():
    return {"message": "Hello from service_223"}
