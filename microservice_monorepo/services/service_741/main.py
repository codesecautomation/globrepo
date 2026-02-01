from fastapi import FastAPI

app = FastAPI(title="service_741")

@app.get("/")
def read_root():
    return {"message": "Hello from service_741"}
