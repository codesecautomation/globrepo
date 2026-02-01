from fastapi import FastAPI

app = FastAPI(title="service_2194")

@app.get("/")
def read_root():
    return {"message": "Hello from service_2194"}
