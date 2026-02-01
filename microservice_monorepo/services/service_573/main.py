from fastapi import FastAPI

app = FastAPI(title="service_573")

@app.get("/")
def read_root():
    return {"message": "Hello from service_573"}
