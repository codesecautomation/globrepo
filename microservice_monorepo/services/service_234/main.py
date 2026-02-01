from fastapi import FastAPI

app = FastAPI(title="service_234")

@app.get("/")
def read_root():
    return {"message": "Hello from service_234"}
