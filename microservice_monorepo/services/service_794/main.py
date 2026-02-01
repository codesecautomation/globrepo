from fastapi import FastAPI

app = FastAPI(title="service_794")

@app.get("/")
def read_root():
    return {"message": "Hello from service_794"}
