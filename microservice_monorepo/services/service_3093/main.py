from fastapi import FastAPI

app = FastAPI(title="service_3093")

@app.get("/")
def read_root():
    return {"message": "Hello from service_3093"}
