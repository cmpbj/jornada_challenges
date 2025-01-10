# FastAPI CRUD Application

This project is a simple CRUD (Create, Read, Update, Delete) application built using FastAPI, SQLAlchemy, and SQLite. It demonstrates how to set up a RESTful API with database interaction.

## Features

- Create items with attributes such as name, price, and offer status.
- Read individual items by their ID.
- Update existing items.
- Delete items from the database.

## Requirements

- Python 3.12
- Poetry (for dependency management)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. Install dependencies using Poetry:
   ```bash
   poetry install
   ```

3. Activate the virtual environment:
   ```bash
   poetry shell
   ```

## Project Structure

```
.
├── main.py        # Entry point of the application
├── schema.py      # Pydantic models for request and response validation
├── models.py      # SQLAlchemy models for database tables
├── database.py    # Database connection and session management
├── first_crud.db  # SQLite database file (auto-created on first run)
```

## Running the Application

1. Start the FastAPI server:
   ```bash
   poetry run uvicorn main:app --reload
   ```

2. Open your browser and navigate to:
   - API Documentation: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - ReDoc Documentation: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## API Endpoints

### Root Endpoint
- **GET** `/`
  - Returns a welcome message.

### Items Endpoints

- **POST** `/items/`
  - Create a new item.
  - Request Body:
    ```json
    {
      "name": "string",
      "price": 0.0,
      "is_offer": true
    }
    ```

- **GET** `/items/{item_id}`
  - Retrieve an item by its ID.

- **PUT** `/items/{item_id}`
  - Update an existing item.
  - Request Body:
    ```json
    {
      "name": "string",
      "price": 0.0,
      "is_offer": true
    }
    ```

- **DELETE** `/items/{item_id}`
  - Delete an item by its ID.

## Database

This project uses SQLite as the database. The database file (`first_crud.db`) is automatically created in the project directory when you run the application for the first time.

## Development

### Adding New Dependencies
To add new dependencies, use Poetry:
```bash
poetry add <package_name>
```

### Updating the Database Schema
If you need to update the database schema, modify the `models.py` file and re-run the application.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)