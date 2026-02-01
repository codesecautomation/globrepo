from fastapi import FastAPI

app = FastAPI(title="service_501")

@app.get("/")
def read_root():
    return {"message": "Hello from service_501"}
