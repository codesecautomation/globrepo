from fastapi import FastAPI

app = FastAPI(title="service_580")

@app.get("/")
def read_root():
    return {"message": "Hello from service_580"}
