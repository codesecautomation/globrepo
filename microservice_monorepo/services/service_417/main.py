from fastapi import FastAPI

app = FastAPI(title="service_417")

@app.get("/")
def read_root():
    return {"message": "Hello from service_417"}
