from fastapi import FastAPI

app = FastAPI(title="service_400")

@app.get("/")
def read_root():
    return {"message": "Hello from service_400"}
