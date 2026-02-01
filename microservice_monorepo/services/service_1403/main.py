from fastapi import FastAPI

app = FastAPI(title="service_1403")

@app.get("/")
def read_root():
    return {"message": "Hello from service_1403"}
