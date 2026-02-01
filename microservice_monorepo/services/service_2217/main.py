from fastapi import FastAPI

app = FastAPI(title="service_2217")

@app.get("/")
def read_root():
    return {"message": "Hello from service_2217"}
