from fastapi import FastAPI

app = FastAPI(title="service_572")

@app.get("/")
def read_root():
    return {"message": "Hello from service_572"}
