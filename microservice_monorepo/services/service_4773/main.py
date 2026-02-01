from fastapi import FastAPI

app = FastAPI(title="service_4773")

@app.get("/")
def read_root():
    return {"message": "Hello from service_4773"}
