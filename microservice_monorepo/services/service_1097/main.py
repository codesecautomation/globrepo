from fastapi import FastAPI

app = FastAPI(title="service_1097")

@app.get("/")
def read_root():
    return {"message": "Hello from service_1097"}
