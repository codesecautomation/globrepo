from fastapi import FastAPI

app = FastAPI(title="service_863")

@app.get("/")
def read_root():
    return {"message": "Hello from service_863"}
