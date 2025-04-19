# RestAPI_opdracht

#Objective:
Develop a RESTful API using Python   and FastAPI   that manages a fun collection of items
(examples: books, movies, boardgames, comics etc.).8

Your API should use SQLAlchemy as an ORM and support all CRUD operations (Create, Read,
Update, Delete).

#Technical Requirements:
• Framework & Tools: FastAPI and SQLAlchemy
• Database: SQLite (or PostgreSQL for bonus points)
• Database Migrations: Provide a folder containing migration scripts as plain SQL files.
• Documentation: Include automated Swagger documentation (FastAPI built-in) and
optionally provide an export from an API testing tool (e.g., Bruno, Insomnia, Postman).

#Required API Endpoints:
Your API must provide the following endpoints:
• POST /items: Add a new item (items must be unique).
• GET /items: Retrieve a list of all items.
• PUT /items/{id}: Update an existing item by ID.
• DELETE /items/{id}: Delete an existing item by ID.

#Evaluation Criteria:
Your submission will be evaluated based on the following criteria:
1. Functionality: All endpoints must work as expected, handling edge cases gracefully.
2. Code Quality: Readable, maintainable, and structured code with proper error handling.
3. Database Design: Appropriate use of SQLAlchemy models and database migrations.
4. Documentation & Testing: Clear Swagger documentation and/or provided test
collections.

#Bonus Points:
• Implement PostgreSQL instead of SQLite.
• Include comprehensive API tests.
• Provide containerization using Docker.

Please submit your completed assignment as a GitHub repository link or a compressed (.zip)
folder containing all relevant files, instructions to run the project, and any other supplementary
materials.