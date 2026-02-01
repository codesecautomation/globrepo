from fastapi import FastAPI

app = FastAPI(title="service_189")

@app.get("/")
def read_root():
    return {"message": "Hello from service_189"}
