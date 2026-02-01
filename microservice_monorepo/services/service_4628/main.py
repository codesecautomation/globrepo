from fastapi import FastAPI

app = FastAPI(title="service_4628")

@app.get("/")
def read_root():
    return {"message": "Hello from service_4628"}
