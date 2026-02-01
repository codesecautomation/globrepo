from fastapi import FastAPI

app = FastAPI(title="service_2006")

@app.get("/")
def read_root():
    return {"message": "Hello from service_2006"}
