from fastapi import FastAPI,Response,HTTPException

app = FastAPI()

@app.get("/entry")
async def read_root():
    return {"message": "Hello World"}