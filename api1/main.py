from fastapi import FastAPI
import requests
import logging

app = FastAPI()
logging.basicConfig(level=logging.INFO)

@app.get("/call-api2")
def call_api2():
    logging.info("API1: Received request from user")
    response = requests.get("http://api2:8002/hello")
    logging.info(f"API1: Got response from API2: {response.text}")
    return {"message_from_api2": response.json()}
