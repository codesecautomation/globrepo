from fastapi import FastAPI

app = FastAPI(title="service_913")

@app.get("/")
def read_root():
    return {"message": "Hello from service_913"}
