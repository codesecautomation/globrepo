from fastapi import FastAPI

app = FastAPI(title="service_4474")

@app.get("/")
def read_root():
    return {"message": "Hello from service_4474"}
