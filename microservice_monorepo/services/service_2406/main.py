from fastapi import FastAPI

app = FastAPI(title="service_2406")

@app.get("/")
def read_root():
    return {"message": "Hello from service_2406"}
