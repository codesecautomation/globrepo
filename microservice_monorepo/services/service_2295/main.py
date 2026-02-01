from fastapi import FastAPI

app = FastAPI(title="service_2295")

@app.get("/")
def read_root():
    return {"message": "Hello from service_2295"}
