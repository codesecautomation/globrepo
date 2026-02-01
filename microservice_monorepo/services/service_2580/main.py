from fastapi import FastAPI

app = FastAPI(title="service_2580")

@app.get("/")
def read_root():
    return {"message": "Hello from service_2580"}
