from fastapi import FastAPI

app = FastAPI(title="service_905")

@app.get("/")
def read_root():
    return {"message": "Hello from service_905"}
