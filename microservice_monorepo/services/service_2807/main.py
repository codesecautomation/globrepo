from fastapi import FastAPI

app = FastAPI(title="service_2807")

@app.get("/")
def read_root():
    return {"message": "Hello from service_2807"}
