from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI()


@app.get("/hello")
async def get_hello():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def get_hello_name(name: str):
    return {"message": "Hello {}".format(name)}


# Define a Pydantic model for the character
class Personnage(BaseModel):
    nom: str
    age: int


# Create a dictionary to store characters
characters_db: Dict[int, Personnage] = {}
characters_db[1] = Personnage(nom="Anne", age=33)
characters_db[2] = Personnage(nom="Michel", age=20)
character_id = 3  # Initial character ID


# Add a character
@app.post("/character/")
def create_character(character: Personnage):
    global character_id
    characters_db[character_id] = character
    character_id += 1
    return character


from fastapi import FastAPI
from pydantic import BaseModel
from starlette import status
import uvicorn

# On instancie le webservice
app = FastAPI()

class Todo(BaseModel):
    id : int
    content : str

todos = {1 : Todo(1,"Step 1 : Learn python")
        , 2 : Todo(2,"Step 2 : Work on the IT project")
        , 3 : Todo(3,"Step 3 : ???")
        , 4 : Todo(4,"Step 4 : Profit")}

# Endpoint GET /todo
@app.get("/todo")
async def get_all_todo():
    return todos.values()

# Endpoint GET /todo/{id_doto}
@app.get("/todo/{id_toto}")
async def get_todo_by_id(id_toto : int = Path(..., description = "The `id` of the todo you want to get")):
    if todos.get[id_toto] :
        return todos.get[id_toto]
    else :
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND)

# Endpoint POST /todo
@app.post("/todo", todo, status_code=201)
async def post_todo(todo:Todo):
    if not todos.get(todo.id):
        return JSONResponse(status_code=status.HTTP_409_CONFLICT)
    else :
        todos[todo.id] = todo
        return todo

# Launch the web service
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)


# Run the FastAPI application
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=5000)
