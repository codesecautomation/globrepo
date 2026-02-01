from fastapi import FastAPI

app = FastAPI(title="service_3354")

@app.get("/")
def read_root():
    return {"message": "Hello from service_3354"}
