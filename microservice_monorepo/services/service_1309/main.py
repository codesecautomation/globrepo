from fastapi import FastAPI

app = FastAPI(title="service_1309")

@app.get("/")
def read_root():
    return {"message": "Hello from service_1309"}
