from fastapi import FastAPI

app = FastAPI(title="service_1223")

@app.get("/")
def read_root():
    return {"message": "Hello from service_1223"}
