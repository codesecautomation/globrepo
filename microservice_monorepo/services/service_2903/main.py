from fastapi import FastAPI

app = FastAPI(title="service_2903")

@app.get("/")
def read_root():
    return {"message": "Hello from service_2903"}
