from fastapi import FastAPI

app = FastAPI(title="service_1821")

@app.get("/")
def read_root():
    return {"message": "Hello from service_1821"}
