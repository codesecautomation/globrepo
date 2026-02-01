from fastapi import FastAPI

app = FastAPI(title="service_2110")

@app.get("/")
def read_root():
    return {"message": "Hello from service_2110"}
