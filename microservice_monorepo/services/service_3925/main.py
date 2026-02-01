from fastapi import FastAPI

app = FastAPI(title="service_3925")

@app.get("/")
def read_root():
    return {"message": "Hello from service_3925"}
