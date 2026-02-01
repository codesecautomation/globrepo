from fastapi import FastAPI

app = FastAPI(title="service_673")

@app.get("/")
def read_root():
    return {"message": "Hello from service_673"}
