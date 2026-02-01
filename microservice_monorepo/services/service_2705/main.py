from fastapi import FastAPI

app = FastAPI(title="service_2705")

@app.get("/")
def read_root():
    return {"message": "Hello from service_2705"}
