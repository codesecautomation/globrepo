from fastapi import FastAPI

app = FastAPI(title="service_2657")

@app.get("/")
def read_root():
    return {"message": "Hello from service_2657"}
