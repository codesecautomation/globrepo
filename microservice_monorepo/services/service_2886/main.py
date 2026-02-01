from fastapi import FastAPI

app = FastAPI(title="service_2886")

@app.get("/")
def read_root():
    return {"message": "Hello from service_2886"}
