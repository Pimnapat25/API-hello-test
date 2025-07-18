from fastapi import FastAPI
import logging

app = FastAPI()
logging.basicConfig(level=logging.INFO)

@app.get("/hello")
def hello():
    logging.info("API2: Received request")
    return {"message": "Hello from API 2"}
