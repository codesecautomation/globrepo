from fastapi import FastAPI

app = FastAPI(title="service_298")

@app.get("/")
def read_root():
    return {"message": "Hello from service_298"}
