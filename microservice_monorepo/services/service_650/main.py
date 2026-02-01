from fastapi import FastAPI

app = FastAPI(title="service_650")

@app.get("/")
def read_root():
    return {"message": "Hello from service_650"}
