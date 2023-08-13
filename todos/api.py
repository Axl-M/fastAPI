from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def welcome() -> dict:
    return {'message': 'Hello World'}



# для запуска в терминале
# uvicorn api:app --port 8080 --reload