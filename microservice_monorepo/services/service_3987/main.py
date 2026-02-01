from fastapi import FastAPI

app = FastAPI(title="service_3987")

@app.get("/")
def read_root():
    return {"message": "Hello from service_3987"}
