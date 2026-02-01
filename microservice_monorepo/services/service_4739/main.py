from fastapi import FastAPI

app = FastAPI(title="service_4739")

@app.get("/")
def read_root():
    return {"message": "Hello from service_4739"}
