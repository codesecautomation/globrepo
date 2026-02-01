from fastapi import FastAPI

app = FastAPI(title="service_381")

@app.get("/")
def read_root():
    return {"message": "Hello from service_381"}
