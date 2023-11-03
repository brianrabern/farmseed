from pymongo import MongoClient
from bson import ObjectId

connection = "mongodb://localhost:27017/"  # if using local mongodb
# connection = "mongodb://database:27017/"  # if using docker-compose

client = MongoClient(connection)
db = client["farmdb"]
collection = db["things"]


def get_all():
    cursor = collection.find()
    things = []

    for thing in cursor:
        thing["_id"] = str(thing["_id"])  # JSON serialization
        things.append(thing)

    return {"things": things}


def get_one(thing_id):
    thing = collection.find_one({"_id": ObjectId(thing_id)})
    thing["_id"] = str(thing["_id"])
    return thing


def post_one(thing):
    collection.insert_one(thing)
    thing["_id"] = str(thing["_id"])
    return thing


def delete_one(thing_id):
    collection.delete_one({"_id": ObjectId(thing_id)})
    return {"status": "deleted"}


def update_one(thing_id, thing):
    updatee = {"_id": ObjectId(thing_id)}
    new_data = {"$set": thing}
    collection.update_one(updatee, new_data)

    updated_thing = collection.find_one(updatee)
    updated_thing["_id"] = str(updated_thing["_id"])

    return updated_thing
