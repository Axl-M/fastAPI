from fastapi import FastAPI
from todo import todo_router
# from model import Todo

app = FastAPI()

@app.get('/')
async def welcome() -> dict:
    return {'message': 'Hello World'}


app.include_router(todo_router)

# для запуска в терминале (из папки где находится приложение!)
# uvicorn api:app --port 8080 --reload
