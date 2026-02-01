from fastapi import FastAPI

app = FastAPI(title="service_3095")

@app.get("/")
def read_root():
    return {"message": "Hello from service_3095"}
