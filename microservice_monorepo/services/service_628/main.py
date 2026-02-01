from fastapi import FastAPI

app = FastAPI(title="service_628")

@app.get("/")
def read_root():
    return {"message": "Hello from service_628"}
