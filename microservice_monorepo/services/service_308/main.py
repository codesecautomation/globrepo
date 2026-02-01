from fastapi import FastAPI

app = FastAPI(title="service_308")

@app.get("/")
def read_root():
    return {"message": "Hello from service_308"}
