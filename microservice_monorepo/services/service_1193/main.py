from fastapi import FastAPI

app = FastAPI(title="service_1193")

@app.get("/")
def read_root():
    return {"message": "Hello from service_1193"}
