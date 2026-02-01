from fastapi import FastAPI

app = FastAPI(title="service_4598")

@app.get("/")
def read_root():
    return {"message": "Hello from service_4598"}
