# API Librería

A modern FastAPI-based REST API for managing a bookstore, with PostgreSQL database integration.

## 🏗️ Project Structure

```
app/
├── src/
│   ├── main.py               # FastAPI application entry point
│   ├── config.py             # Application configuration
│   ├── database.py           # Database connection and session management
│   ├── dependencies.py       # Shared dependencies (e.g., get_db)
│   ├── models.py             # SQLAlchemy ORM models
│   ├── schemas.py            # Pydantic schemas for validation
│   ├── crud.py               # Database operations (CRUD)
│   └── routers/
│       └── books.py          # Book-related endpoints
├── requirements.txt          # Python dependencies
├── Dockerfile               # Docker configuration
└── .env.example             # Environment variables template
```

## 🚀 Features

- **RESTful API** with FastAPI
- **Database**: PostgreSQL with SQLAlchemy ORM
- **Validation**: Pydantic schemas with field validation
- **CRUD Operations**: Complete book management
- **Search**: Filter books by name, author, or ISBN
- **Stock Management**: Track and manage book inventory
- **Docker Support**: Containerized application
- **Auto Documentation**: Swagger UI and ReDoc

## 📋 Prerequisites

- Docker and Docker Compose
- Python 3.13+ (for local development)

## 🔧 Installation & Setup

### Using Docker (Recommended)

1. Clone the repository
2. Start the services:
```bash
docker-compose up -d
```

The API will be available at `http://localhost:8000`

### Local Development

1. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r app/requirements.txt
```

3. Set up environment variables:
```bash
cp app/.env.local app/.env
# Edit app/.env with your configuration
```

4. Run the application:
```bash
cd app
uvicorn src.main:app --reload
```

## 📚 API Endpoints

### Root
- `GET /` - Welcome message and API info
- `GET /health` - Health check

### Books
- `GET /books/` - Get all books (with pagination)
- `GET /books/search` - Search books by name, author, or ISBN
- `GET /books/{book_id}` - Get a specific book
- `POST /books/{book_id}/buy` - Purchase a book (decrease stock)

## 📖 API Documentation

Once the application is running, visit:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🗄️ Database Schema

### Books Table
- `id` (Integer, Primary Key)
- `name` (String, Required, Indexed)
- `author` (String, Required, Indexed)
- `isbn` (String, Unique, Required, Indexed)
- `published_at` (Date, Optional)
- `price` (Numeric, Optional)
- `stock` (Integer, Default: 0)

## 🔒 Environment Variables

Create a `.env` file based on `.env.example`:

```env
DATABASE_URL=postgresql://admin:admin@db:5432/library_db
APP_NAME=API Librería
APP_VERSION=1.0.0
DEBUG=False
```

## 🛠️ Development

### Project Structure Best Practices

This project follows FastAPI best practices:

1. **Separation of Concerns**
   - `models.py`: Database models (ORM)
   - `schemas.py`: Request/response models (Pydantic)
   - `crud.py`: Database operations
   - `routers/`: API endpoints
   - `dependencies.py`: Shared dependencies

2. **Configuration Management**
   - Centralized in `config.py`
   - Uses `pydantic-settings` for validation
   - Environment variable support

3. **Database Management**
   - Connection pooling
   - Session management with dependency injection
   - Automatic table creation on startup

4. **API Design**
   - RESTful conventions
   - Proper HTTP status codes
   - Comprehensive error handling
   - Request/response validation

## 🧪 Testing

To test the API, you can use:
- The interactive Swagger UI at `/docs`
- curl commands
- Postman or similar tools

Example curl commands:
```bash
# Get all books
curl "http://localhost:8000/books/"

# Search books
curl "http://localhost:8000/books/search?author=Cervantes"

# Get a specific book
curl "http://localhost:8000/books/1"

# Buy a book
curl -X POST "http://localhost:8000/books/1/buy"
```

## 🐳 Docker Commands

```bash
# Start services
docker-compose up -d

# View logs
docker-compose logs -f api

# Stop services
docker-compose down

# Rebuild after changes
docker-compose up -d --build

# Access database
docker exec -it library_db psql -U admin -d library_db
```

## 📝 License

This project is open source and available under the MIT License.
