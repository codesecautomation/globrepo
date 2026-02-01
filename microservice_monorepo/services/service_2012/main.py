from fastapi import FastAPI

app = FastAPI(title="service_2012")

@app.get("/")
def read_root():
    return {"message": "Hello from service_2012"}
