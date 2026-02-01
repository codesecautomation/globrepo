from fastapi import FastAPI

app = FastAPI(title="service_2888")

@app.get("/")
def read_root():
    return {"message": "Hello from service_2888"}
