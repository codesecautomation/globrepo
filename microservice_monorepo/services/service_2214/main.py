from fastapi import FastAPI

app = FastAPI(title="service_2214")

@app.get("/")
def read_root():
    return {"message": "Hello from service_2214"}
