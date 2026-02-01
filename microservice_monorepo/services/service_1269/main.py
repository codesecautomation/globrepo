from fastapi import FastAPI

app = FastAPI(title="service_1269")

@app.get("/")
def read_root():
    return {"message": "Hello from service_1269"}
