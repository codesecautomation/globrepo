from fastapi import FastAPI

app = FastAPI(title="service_4996")

@app.get("/")
def read_root():
    return {"message": "Hello from service_4996"}
