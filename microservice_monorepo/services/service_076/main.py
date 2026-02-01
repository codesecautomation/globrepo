from fastapi import FastAPI

app = FastAPI(title="service_076")

@app.get("/")
def read_root():
    return {"message": "Hello from service_076"}
