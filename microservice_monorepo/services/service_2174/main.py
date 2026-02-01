from fastapi import FastAPI

app = FastAPI(title="service_2174")

@app.get("/")
def read_root():
    return {"message": "Hello from service_2174"}
