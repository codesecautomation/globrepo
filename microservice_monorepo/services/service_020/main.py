from fastapi import FastAPI

app = FastAPI(title="service_020")

@app.get("/")
def read_root():
    return {"message": "Hello from service_020"}
