from fastapi import FastAPI

app = FastAPI(title="service_4676")

@app.get("/")
def read_root():
    return {"message": "Hello from service_4676"}
