from fastapi import FastAPI

app = FastAPI(title="service_3490")

@app.get("/")
def read_root():
    return {"message": "Hello from service_3490"}
