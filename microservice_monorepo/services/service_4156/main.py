from fastapi import FastAPI

app = FastAPI(title="service_4156")

@app.get("/")
def read_root():
    return {"message": "Hello from service_4156"}
