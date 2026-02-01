from fastapi import FastAPI

app = FastAPI(title="service_2051")

@app.get("/")
def read_root():
    return {"message": "Hello from service_2051"}
