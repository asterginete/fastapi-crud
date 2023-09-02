/fastapi-crud
│
├── /app
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── /models
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── item.py
│   │   ├── order.py       # New: Order-related database models
│   │   └── review.py      # New: Review-related database models
│   ├── /schemas
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── item.py
│   │   ├── order.py       # New: Order-related Pydantic models
│   │   └── review.py      # New: Review-related Pydantic models
│   ├── /crud
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── item.py
│   │   ├── order.py       # New: CRUD operations for orders
│   │   └── review.py      # New: CRUD operations for reviews
│   ├── /deps
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   └── db.py
│   ├── /api
│   │   ├── __init__.py
│   │   └── /v1
│   │       ├── __init__.py
│   │       ├── items.py
│   │       ├── users.py
│   │       ├── orders.py  # New: Routes related to orders
│   │       └── reviews.py # New: Routes related to reviews
│   ├── /services
│   │   ├── __init__.py
│   │   ├── email.py
│   │   ├── image.py
│   │   ├── payment.py     # New: Payment processing operations
│   │   └── shipping.py    # New: Shipping-related operations
│   └── /core
│       ├── __init__.py
│       ├── security.py
│       ├── validation.py  # New: Additional validation utilities
│       └── notifications.py # New: Core utilities for notifications
│
├── /migrations
│
├── /tests
│   ├── __init__.py
│   ├── test_users.py
│   ├── test_items.py
│   ├── test_orders.py    # New: Test cases for orders
│   └── test_reviews.py   # New: Test cases for reviews
│
├── /static
│
├── /templates
│
├── Dockerfile
├── .env
├── README.md
└── requirements.txt
