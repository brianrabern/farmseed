from fastapi import FastAPI

# from database_sql import get_all, get_one, post_one, update_one, delete_one

from database import get_all, get_one, post_one, update_one, delete_one
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/things")
def get_all_things():
    return get_all()


@app.get("/things/{thing_id}")
def get_one_thing(thing_id: str):
    return get_one(thing_id)


@app.post("/things")
def post_one_thing(thing: dict):
    return post_one(thing)


@app.put("/things/{thing_id}")
def update_one_thing(thing_id: str, thing: dict):
    return update_one(thing_id, thing)


@app.delete("/things/{thing_id}")
def delete_one_thing(thing_id: str):
    return delete_one(thing_id)
