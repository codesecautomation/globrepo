from fastapi import FastAPI

app = FastAPI(title="service_977")

@app.get("/")
def read_root():
    return {"message": "Hello from service_977"}
