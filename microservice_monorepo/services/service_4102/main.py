from fastapi import FastAPI

app = FastAPI(title="service_4102")

@app.get("/")
def read_root():
    return {"message": "Hello from service_4102"}
