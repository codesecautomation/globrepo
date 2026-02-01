from fastapi import FastAPI

app = FastAPI(title="service_4492")

@app.get("/")
def read_root():
    return {"message": "Hello from service_4492"}
