from fastapi import FastAPI

app = FastAPI(title="service_678")

@app.get("/")
def read_root():
    return {"message": "Hello from service_678"}
