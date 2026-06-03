# E-commerce API

REST API for e-commerce management with JWT authentication and role-based access control.

## Tech Stack

- **FastAPI** — Python web framework
- **PostgreSQL** — Database
- **SQLAlchemy** — ORM
- **bcrypt** — Password hashing
- **python-jose** — JWT tokens
- **Docker** — Containerization
- **pytest** — Testing

## Features

- JWT authentication
- Role-based access control (admin / user)
- Product management
- Order management with stock validation
- Automatic total calculation

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Run the project

```bash
git clone git@github.com:vanDevBett/ecommerce-api.git
cd ecommerce-api
cp .env.example .env
docker compose up --build
```

API available at `http://localhost:8000`

Interactive documentation at `http://localhost:8000/docs`

## API Endpoints

### Auth
| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| POST | /auth/register | Register a new user | No |
| POST | /auth/login | Login and get JWT token | No |

### Products
| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| GET | /products | Get all products | No |
| GET | /products/{id} | Get a product | No |
| POST | /products | Create a product | Admin |
| PUT | /products/{id} | Update a product | Admin |
| DELETE | /products/{id} | Delete a product | Admin |

### Orders
| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| POST | /orders | Create an order | User |
| GET | /orders | Get my orders | User |
| GET | /orders/{id} | Get an order | User |

## Run Tests

```bash
pytest tests/ -v
```

## Project Structure

```
app/
├── api/          # Endpoints
├── core/         # Config, database, security, dependencies
├── models/       # Database models
├── schemas/      # Pydantic schemas
├── services/     # Business logic
└── main.py       # Entry point
```