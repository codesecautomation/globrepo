from fastapi import FastAPI

app = FastAPI(title="service_3275")

@app.get("/")
def read_root():
    return {"message": "Hello from service_3275"}
