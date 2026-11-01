from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Backend berjaya dijalankan!"}

@app.get("/test")
def test():
    return {"status": "success"}