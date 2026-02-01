from fastapi import FastAPI

app = FastAPI(title="service_256")

@app.get("/")
def read_root():
    return {"message": "Hello from service_256"}
