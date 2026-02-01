from fastapi import FastAPI

app = FastAPI(title="service_506")

@app.get("/")
def read_root():
    return {"message": "Hello from service_506"}
