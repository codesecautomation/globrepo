from fastapi import FastAPI

app = FastAPI(title="service_972")

@app.get("/")
def read_root():
    return {"message": "Hello from service_972"}
