from fastapi import FastAPI

app = FastAPI(title="service_125")

@app.get("/")
def read_root():
    return {"message": "Hello from service_125"}
