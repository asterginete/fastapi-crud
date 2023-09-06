# FastAPI E-commerce Backend

This project is a backend API for an e-commerce platform built using FastAPI. It provides endpoints for user management, item listing, order processing, reviews, and more.

## Features

- User registration and authentication
- CRUD operations for items
- Order processing
- User reviews for items
- Email notifications (mocked)
- Image processing (mocked)
- Payment processing (mocked)
- Shipping calculations (mocked)

## Requirements

- Python 3.9+
- PostgreSQL
- Docker (optional for containerized deployment)

## Setup & Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/fastapi_project.git
    cd fastapi_project
    ```

2. **Set up a virtual environment and install dependencies:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```

3. **Environment Variables:**

    Create a `.env` file in the root directory and set the following variables:

    ```
    DATABASE_URL=postgresql://username:password@localhost:5432/fastapi_db
    SECRET_KEY=your_secret_key
    ALGORITHM=HS256
    EMAIL_USERNAME=your_email@example.com
    EMAIL_PASSWORD=your_email_password
    ```

    Replace placeholders with your actual values.

4. **Database Setup:**

    Ensure PostgreSQL is running and the specified database exists. The application will handle table creation on startup.

5. **Run the application:**

    ```bash
    uvicorn app.main:app --reload
    ```

    The API will be available at `http://127.0.0.1:8000/`.

## Docker Deployment

1. **Build the Docker image:**

    ```bash
    docker build -t fastapi_app .
    ```

2. **Run the Docker container:**

    ```bash
    docker run -p 8000:8000 fastapi_app
    ```

    The API will be available at `http://127.0.0.1:8000/`.

## API Endpoints

- `/users/`: User registration
- `/login/`: User authentication
- `/items/`: CRUD operations for items
- `/orders/`: Order processing
- `/reviews/`: User reviews for items

## Testing

To run the tests:

```bash
pytest
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License.
