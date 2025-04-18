from model import Todo
#MongoDB Driver
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb+srv://<db_user>:<db_password>@cluster0.tevmv.mongodb.net/?retryWrites=true&w=majority')
# Ensure to replace <db_user> & <db_password> with your actual MongoDB username and password.
database = client.TodoList
collection = database.todo

async def fetch_one_todo(id):
    document = await collection.find_one({"id": id})
    return document

async def fetch_all_todos():
    todos = []
    cursor = collection.find({})
    async for document in cursor:
        todos.append(Todo(**document))
    return todos

async def create_todo(todo):
    document = todo
    result = await collection.insert_one(document)
    return document

async def update_todo(id, todo):
    await collection.update_one({"id": id}, {"$set": todo})
    document = await collection.find_one({"id": id})
    return document

async def remove_todo(id):
    await collection.delete_one({"id": id})
    return True