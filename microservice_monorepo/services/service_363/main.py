from fastapi import FastAPI

app = FastAPI(title="service_363")

@app.get("/")
def read_root():
    return {"message": "Hello from service_363"}
