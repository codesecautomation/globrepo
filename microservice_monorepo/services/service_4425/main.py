from fastapi import FastAPI

app = FastAPI(title="service_4425")

@app.get("/")
def read_root():
    return {"message": "Hello from service_4425"}
