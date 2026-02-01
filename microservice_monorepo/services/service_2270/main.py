from fastapi import FastAPI

app = FastAPI(title="service_2270")

@app.get("/")
def read_root():
    return {"message": "Hello from service_2270"}
