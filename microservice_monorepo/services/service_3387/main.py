from fastapi import FastAPI

app = FastAPI(title="service_3387")

@app.get("/")
def read_root():
    return {"message": "Hello from service_3387"}
