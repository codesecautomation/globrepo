from fastapi import FastAPI

app = FastAPI(title="service_4847")

@app.get("/")
def read_root():
    return {"message": "Hello from service_4847"}
