from fastapi import FastAPI

app = FastAPI(title="service_101")

@app.get("/")
def read_root():
    return {"message": "Hello from service_101"}
