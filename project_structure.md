/fastapi-crud
│
├── /app
│   ├── __init__.py
│   ├── main.py            # Main FastAPI application
│   ├── config.py          # Configuration and environment variables
│   ├── /models
│   │   ├── __init__.py
│   │   ├── user.py        # User-related database models
│   │   ├── item.py        # Item-related database models
│   │   └── ...            # Other database models
│   ├── /schemas
│   │   ├── __init__.py
│   │   ├── user.py        # User-related Pydantic models
│   │   ├── item.py        # Item-related Pydantic models
│   │   └── ...            # Other Pydantic models
│   ├── /crud
│   │   ├── __init__.py
│   │   ├── user.py        # CRUD operations for users
│   │   ├── item.py        # CRUD operations for items
│   │   └── ...            # CRUD operations for other entities
│   ├── /deps
│   │   ├── __init__.py
│   │   ├── auth.py        # Authentication dependencies
│   │   └── db.py          # Database session dependency
│   ├── /api
│   │   ├── __init__.py
│   │   └── /v1
│   │       ├── __init__.py
│   │       ├── items.py   # Routes related to items
│   │       ├── users.py   # Routes related to users
│   │       └── ...        # Other routes
│   ├── /services
│   │   ├── __init__.py
│   │   ├── email.py       # Email-related operations
│   │   ├── image.py       # Image processing operations
│   │   └── ...            # Other services
│   └── /core
│       ├── __init__.py
│       ├── security.py    # Security-related utilities (e.g., password hashing)
│       └── ...            # Other core utilities
│
├── /migrations            # Alembic migrations directory
│
├── /tests                 # Test cases and fixtures
│   ├── __init__.py
│   ├── test_users.py
│   ├── test_items.py
│   └── ...
│
├── /static                # Static files (e.g., images, CSS)
│
├── /templates             # Jinja2 templates for email, etc.
│
├── Dockerfile             # Docker configuration file
├── .env                   # Environment variables
├── README.md
└── requirements.txt       # List of Python dependencies
