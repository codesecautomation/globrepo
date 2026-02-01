from fastapi import FastAPI

app = FastAPI(title="service_895")

@app.get("/")
def read_root():
    return {"message": "Hello from service_895"}
