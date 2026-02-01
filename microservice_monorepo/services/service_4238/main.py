from fastapi import FastAPI

app = FastAPI(title="service_4238")

@app.get("/")
def read_root():
    return {"message": "Hello from service_4238"}
