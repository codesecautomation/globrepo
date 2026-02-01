from fastapi import FastAPI

app = FastAPI(title="service_156")

@app.get("/")
def read_root():
    return {"message": "Hello from service_156"}
