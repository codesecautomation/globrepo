from fastapi import FastAPI

app = FastAPI(title="service_4160")

@app.get("/")
def read_root():
    return {"message": "Hello from service_4160"}
