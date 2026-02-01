from fastapi import FastAPI

app = FastAPI(title="service_522")

@app.get("/")
def read_root():
    return {"message": "Hello from service_522"}
