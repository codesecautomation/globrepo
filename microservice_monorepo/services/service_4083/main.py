from fastapi import FastAPI

app = FastAPI(title="service_4083")

@app.get("/")
def read_root():
    return {"message": "Hello from service_4083"}
