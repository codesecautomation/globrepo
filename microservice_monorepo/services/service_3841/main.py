from fastapi import FastAPI

app = FastAPI(title="service_3841")

@app.get("/")
def read_root():
    return {"message": "Hello from service_3841"}
