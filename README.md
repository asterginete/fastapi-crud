# FastAPI CRUD API with PostgreSQL

This is a CRUD API built using FastAPI that provides endpoints to manage a collection of items. The API features token-based authentication, authorization, data validation, and uses PostgreSQL as its database.

## Prerequisites

- Python 3.7 or higher
- PostgreSQL

## Installation

1. **Set Up a Virtual Environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

2. **Install Required Packages**:
   ```bash
   pip install fastapi[all] uvicorn sqlalchemy asyncpg databases passlib[jwt] jose
   ```

3. **Configure Database**:
   - Ensure you have a running PostgreSQL instance.
   - Create a new database for the application.
   - Update the `DATABASE_URL` in the application code with your PostgreSQL credentials and database details.

4. **Run the Application**:
   ```bash
   uvicorn main:app --reload
   ```

## Features

- **CRUD Operations**: Create, read, update, and delete items.
- **Authentication**: Token-based authentication using JWT.
- **Authorization**: Role-based authorization to restrict access to certain routes.
- **Data Validation**: Input and data validation using Pydantic.
- **Database**: PostgreSQL integration using SQLAlchemy and asyncpg.

## Endpoints

- **Token Generation**: `POST /token`
- **Create an Item**: `POST /items/`
- **Retrieve All Items**: `GET /items/`
- **Retrieve a Specific Item by ID**: `GET /items/{item_id}`
- **Update a Specific Item by ID**: `PUT /items/{item_id}`
- **Delete a Specific Item by ID**: `DELETE /items/{item_id}`

## Contributing

If you'd like to contribute, please fork the repository and make changes as you'd like. Pull requests are warmly welcome.

## License

This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).
