from fastapi import FastAPI

app = FastAPI(title="service_570")

@app.get("/")
def read_root():
    return {"message": "Hello from service_570"}
