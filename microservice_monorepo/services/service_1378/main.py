from fastapi import FastAPI

app = FastAPI(title="service_1378")

@app.get("/")
def read_root():
    return {"message": "Hello from service_1378"}
