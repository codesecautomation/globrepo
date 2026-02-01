from fastapi import FastAPI

app = FastAPI(title="service_2308")

@app.get("/")
def read_root():
    return {"message": "Hello from service_2308"}
