from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Creatify Video API")

app.include_router(router)

@app.get("/")
def root():
    return {"message": "Welcome to the Creatify Video API. Use /docs to test the API."}