from fastapi import FastAPI

app = FastAPI(title="service_2276")

@app.get("/")
def read_root():
    return {"message": "Hello from service_2276"}
