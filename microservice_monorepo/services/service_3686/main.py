from fastapi import FastAPI

app = FastAPI(title="service_3686")

@app.get("/")
def read_root():
    return {"message": "Hello from service_3686"}
