from fastapi import FastAPI

app = FastAPI(title="service_3396")

@app.get("/")
def read_root():
    return {"message": "Hello from service_3396"}
