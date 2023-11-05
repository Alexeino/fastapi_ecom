from fastapi import FastAPI

app = FastAPI(title="Ecommerce API")


@app.get("/")
def health():
    return {"message": "OK"}
