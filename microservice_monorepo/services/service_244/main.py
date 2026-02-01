from fastapi import FastAPI

app = FastAPI(title="service_244")

@app.get("/")
def read_root():
    return {"message": "Hello from service_244"}
