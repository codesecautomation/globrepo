from fastapi import FastAPI

app = FastAPI(title="service_832")

@app.get("/")
def read_root():
    return {"message": "Hello from service_832"}
