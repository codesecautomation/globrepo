from fastapi import FastAPI

app = FastAPI(title="service_336")

@app.get("/")
def read_root():
    return {"message": "Hello from service_336"}
