from fastapi import FastAPI

app = FastAPI(title="service_1603")

@app.get("/")
def read_root():
    return {"message": "Hello from service_1603"}
