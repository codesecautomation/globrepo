from fastapi import FastAPI

app = FastAPI(title="service_4908")

@app.get("/")
def read_root():
    return {"message": "Hello from service_4908"}
