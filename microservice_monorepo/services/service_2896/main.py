from fastapi import FastAPI

app = FastAPI(title="service_2896")

@app.get("/")
def read_root():
    return {"message": "Hello from service_2896"}
