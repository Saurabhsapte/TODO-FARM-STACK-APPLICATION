from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from model import Todo,TodoDto

from database import (
    fetch_one_todo,
    fetch_all_todos,
    create_todo,
    update_todo,
    remove_todo
)
# from fastapi.responses import JSONResponse
# App Object
app = FastAPI()

origins = ['https://localhost:5173', 'http://localhost:5173']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/v1/todos", response_model=list[Todo])
async def get_todo():
    response = await fetch_all_todos()
    return response

@app.get("/api/v1/todo{id}", response_model=Todo)
async def get_todo_by_id(id: int):
    response = await fetch_one_todo(id)
    if not response:
        raise HTTPException(status_code=404, detail=f"There is no TODO item with id {id}")
    return response

@app.post("/api/v1/todo", response_model=Todo)
async def post_todo(todo: Todo):
    response = await create_todo(todo.dict())
    return response

@app.put("/api/v1/todo{id}", response_model=Todo)
async def put_todo(id: int, todo: TodoDto):
    response = await update_todo(id, todo.dict())
    if not response:
        raise HTTPException(status_code=404, detail=f"There is no TODO item with id {id}")
    return response

@app.delete("/api/v1/todo{id}", response_model=dict)
async def delete_todo(id: int):
    response = await remove_todo(id)
    if not response:
        raise HTTPException(status_code=404, detail=f"There is no TODO item with id {id}")
    return {"message": "Todo deleted successfully"}