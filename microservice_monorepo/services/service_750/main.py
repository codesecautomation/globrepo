from fastapi import FastAPI

app = FastAPI(title="service_750")

@app.get("/")
def read_root():
    return {"message": "Hello from service_750"}
