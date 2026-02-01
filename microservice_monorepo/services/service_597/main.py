from fastapi import FastAPI

app = FastAPI(title="service_597")

@app.get("/")
def read_root():
    return {"message": "Hello from service_597"}
