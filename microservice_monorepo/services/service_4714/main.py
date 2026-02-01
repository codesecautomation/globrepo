from fastapi import FastAPI

app = FastAPI(title="service_4714")

@app.get("/")
def read_root():
    return {"message": "Hello from service_4714"}
