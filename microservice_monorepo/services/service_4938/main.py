from fastapi import FastAPI

app = FastAPI(title="service_4938")

@app.get("/")
def read_root():
    return {"message": "Hello from service_4938"}
