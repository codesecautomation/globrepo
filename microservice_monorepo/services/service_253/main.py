from fastapi import FastAPI

app = FastAPI(title="service_253")

@app.get("/")
def read_root():
    return {"message": "Hello from service_253"}
