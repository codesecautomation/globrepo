from fastapi import FastAPI

app = FastAPI(title="service_561")

@app.get("/")
def read_root():
    return {"message": "Hello from service_561"}
