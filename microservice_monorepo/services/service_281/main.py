from fastapi import FastAPI

app = FastAPI(title="service_281")

@app.get("/")
def read_root():
    return {"message": "Hello from service_281"}
