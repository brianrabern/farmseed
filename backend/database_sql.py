import mysql.connector


def db_access():
    connection = mysql.connector.connect(
        user="admin",
        password="password",
        host="127.0.0.1",
        port=3306,
        database="farmsql",
    )
    cursor = connection.cursor(dictionary=True)
    return connection, cursor


def get_all():
    query = "SELECT * FROM things"
    cursor = None
    try:
        connection, cursor = db_access()
        cursor.execute(query)

        things = []

        for thing in cursor:
            thing["_id"] = str(thing["_id"])
            things.append(thing)

        return {"things": things}
    finally:
        cursor.close() if cursor else None
        connection.close() if connection else None


def get_one(thing_id):
    query = "SELECT * FROM things WHERE _id = %s"
    cursor = None
    try:
        connection, cursor = db_access()
        cursor.execute(query, [int(thing_id)])
        thing = cursor.fetchone()
        thing["_id"] = str(thing["_id"])
        return thing
    finally:
        cursor.close() if cursor else None
        connection.close() if connection else None


def post_one(thing):
    insert_query = "INSERT INTO things (name, description) VALUES (%(name)s, %(description)s)"  # noqa

    values = {"name": thing["name"], "description": thing["description"]}
    cursor = None
    try:
        connection, cursor = db_access()
        cursor.execute(insert_query, values)
        connection.commit()

        new_thing_id = cursor.lastrowid
        select_query = "SELECT * FROM things WHERE _id = %s"
        cursor.execute(select_query, [new_thing_id])
        thing = cursor.fetchone()
        thing["_id"] = str(thing["_id"])

        return thing
    finally:
        cursor.close() if cursor else None
        connection.close() if connection else None


def update_one(thing_id, thing):
    update_query = "UPDATE things SET "
    update_values = {}

    for key, value in thing.items():
        update_query += f"{key} = %({key})s, "
        update_values[key] = value

    update_query = update_query[:-2]
    update_query += " WHERE _id = %(_id)s"
    update_values["_id"] = int(thing_id)

    cursor = None

    try:
        connection, cursor = db_access()
        cursor.execute(update_query, update_values)
        connection.commit()

        updated_thing = get_one(thing_id)
        updated_thing["_id"] = str(updated_thing["_id"])
        return updated_thing
    finally:
        cursor.close() if cursor else None
        connection.close() if connection else None


def delete_one(thing_id):
    cursor = None
    try:
        connection, cursor = db_access()
        cursor.execute("DELETE FROM things WHERE _id = %s", [int(thing_id)])
        connection.commit()

        return (
            {"status": "success", "deleted_thing": thing_id}
            if cursor.rowcount
            else {"status": "failed"}
        )

    finally:
        cursor.close() if cursor else None
        connection.close() if connection else None
