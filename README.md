# FARM seed

A seed project for building web applications using the FARM stack - FastAPI, React, and MongoDB.

![Screenshot](farm_wire.png)

## About

This project provides a starting point for building a web app using Python's FastAPI for the backend, React for the frontend, and MongoDB as the database. It includes basic scaffolding of each component to get started.

## Getting Started

There are two options: (i) Local Development: You can spin it up on locahost or (ii) Docker: use the provided docker files to spin it up in Docker containers. Both options are outlined below.

### Option (i): Localhost Installation

Ensure you have the following prerequisites installed on your development environment:

- Python 3.7+
- Node.js
- MongoDB

1. Clone the repo

   ```bash
   git clone https://github.com/brianrabern/farmseed.git
   ```

2. Set up MongoDB

   a. Download and install MongoDB Community Server edition. (On macOS: `brew install mongodb`)

   b. Create data directory:

   ```bash
   mkdir ~/data
   mkdir ~/data/db
   ```

   c. Run MongoDB daemon:

   ```bash
   mongod --dbpath ~/data/db
   ```

   d. In the MongoDB Shell add a db and put a thing in a collection:

   ```bash
   mongosh
   ```

   ```sql
   > use farmdb
   > db.createCollection("things")
   > db.things.insertOne({"name":"Thing1","description":"A thing that shines"})
   ```

3. Set up FastAPI backend

   - `cd backend`
   - `pip install -r requirements.txt`
   - `uvicorn main:app --reload`

4. Set up React frontend

   - `cd frontend`
   - `npm install`
   - `npm start`

The FastAPI backend will run on `http://localhost:8000`.
The React frontend will run on `http://localhost:3000`.

### Option (ii): Docker Containers

Ensure you have Docker installed.

1. Clone the repo, and cd into it.

   ```bash
   git clone https://github.com/brianrabern/farmseed.git
   cd farmseed
   ```

2. Update main.py:

   Open the backend/main.py file.

   Comment out the local MongoDB connection string and uncomment the Docker Compose MongoDB connection string:

   ```python
   # connection = "mongodb://localhost:27017/"
   connection = "mongodb://database:27017/"
   ```

3. Docker build and spin up:

```bash
docker-compose build
docker-compose up
```

## Bonus: SQL

If you'd like to use a relational database instead, you can replace the MongoDB with MySQL (or MariaDB) or PostgreSQL. Here is the basics for MariaDB using mysql.connector. These instructions are for localhost.

1. **Install MariaDB:**
   a. Download and install MariaDB.

   ```bash
   brew install mariadb
   ```

   b. Start MariaDB service:

   ```bash
   brew services start mariadb
   ```

2. **Set Up MariaDB Database:**
   a. Access the MariaDB shell:

   ```bash
   mysql
   ```

   b. Create a database and switch to it:

   ```sql
   CREATE DATABASE farmsql;
   USE farmsql;
   ```

   c. Create a table named `things`:

   ```sql
   CREATE TABLE `things` (
       _id INT AUTO_INCREMENT PRIMARY KEY,
       name VARCHAR(255) DEFAULT NULL,
       description VARCHAR(255) DEFAULT NULL
   );
   ```

   d. Insert a sample record into the `things` table:

   ```sql
   INSERT INTO things (name, description) VALUES ('Thing1', 'A thing that shines');
   ```

3. Switch from using MongoDB to MariaDB (SQL) in the `main.py` file.

   a. Comment out the MongoDB-related imports:

   ```python
   # from database import get_all, get_one, post_one, update_one, delete_one
   ```

   b. Uncomment the SQL-related imports:

   ```python
   from database_sql import get_all, get_one, post_one, update_one, delete_one
   ```

## Usage

The FastAPI backend offers essential API endpoints for standard CRUD (Create, Read, Update, Delete) operations. The React frontend includes sample components that correspond to these endpoints, providing a starting point for your user interface.

You can extend or adjust the project's functionality by:

- Defining Pydantic models for your data.
- Expanding the range of React components, add detail page, etc..
- Implementing user authentication for enhanced security.
- Set up unit tests and integration tests
- Replace or supplement the use of the built-in fetch API with Axios

With FARM seed, you have a versatile and well-structured base for building web applications using the FARM stack. Feel free to tailor it to your specific project requirements and scale it as needed.

-- B.Rabern::2023 --
