from fastapi import FastAPI

app = FastAPI(title="service_3769")

@app.get("/")
def read_root():
    return {"message": "Hello from service_3769"}
