from pymongo import MongoClient
from bson import ObjectId


def db_access():
    # connection = "mongodb://database:27017/"  # if using docker-compose
    connection = "mongodb://localhost:27017/"  # if using local mongodb
    client = MongoClient(connection)
    db = client["farmdb"]
    collection = db["things"]
    return collection


def get_all():
    collection = db_access()
    cursor = collection.find()
    things = []

    for thing in cursor:
        thing["_id"] = str(thing["_id"])  # JSON serialization
        things.append(thing)

    return {"things": things}


def get_one(thing_id):
    collection = db_access()
    thing = collection.find_one({"_id": ObjectId(thing_id)})
    thing["_id"] = str(thing["_id"])
    return thing


def post_one(thing):
    collection = db_access()
    collection.insert_one(thing)
    thing["_id"] = str(thing["_id"])
    return thing


def update_one(thing_id, thing):
    collection = db_access()
    updatee = {"_id": ObjectId(thing_id)}
    new_data = {"$set": thing}
    collection.update_one(updatee, new_data)

    updated_thing = collection.find_one(updatee)
    updated_thing["_id"] = str(updated_thing["_id"])

    return updated_thing


def delete_one(thing_id):
    collection = db_access()
    result = collection.delete_one({"_id": ObjectId(thing_id)})
    return (
        {"status": "success", "deleted_thing": thing_id}
        if result.deleted_count
        else {"status": "failed"}
    )
