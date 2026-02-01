from fastapi import FastAPI

app = FastAPI(title="service_961")

@app.get("/")
def read_root():
    return {"message": "Hello from service_961"}
