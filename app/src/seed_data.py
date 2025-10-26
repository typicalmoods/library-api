"""
Script to populate the database with initial test data
"""
from datetime import date
from sqlalchemy.orm import Session
from .database import SessionLocal, engine, Base
from .models import Book


def create_seed_data(db: Session) -> None:
    """Create initial test data for the library database"""
    
    # Check if data already exists
    existing_books = db.query(Book).count()
    if existing_books > 0:
        print(f"Database already contains {existing_books} books. Skipping seed data creation.")
        return
    
    # Sample books data
    books_data = [
        {
            "name": "Cien años de soledad",
            "author": "Gabriel García Márquez",
            "isbn": "9780307474728",
            "published_at": date(1967, 6, 5),
            "price": 19.99,
            "stock": 15
        },
        {
            "name": "Don Quijote de la Mancha",
            "author": "Miguel de Cervantes",
            "isbn": "9788420412146",
            "published_at": date(1605, 1, 16),
            "price": 24.50,
            "stock": 10
        },
        {
            "name": "1984",
            "author": "George Orwell",
            "isbn": "9780451524935",
            "published_at": date(1949, 6, 8),
            "price": 15.99,
            "stock": 20
        },
        {
            "name": "El principito",
            "author": "Antoine de Saint-Exupéry",
            "isbn": "9780156012195",
            "published_at": date(1943, 4, 6),
            "price": 12.99,
            "stock": 25
        },
        {
            "name": "Crónica de una muerte anunciada",
            "author": "Gabriel García Márquez",
            "isbn": "9780307387387",
            "published_at": date(1981, 1, 1),
            "price": 16.99,
            "stock": 8
        },
        {
            "name": "La sombra del viento",
            "author": "Carlos Ruiz Zafón",
            "isbn": "9788408163251",
            "published_at": date(2001, 4, 17),
            "price": 21.99,
            "stock": 12
        },
        {
            "name": "El amor en los tiempos del cólera",
            "author": "Gabriel García Márquez",
            "isbn": "9780307389732",
            "published_at": date(1985, 1, 1),
            "price": 18.99,
            "stock": 7
        },
        {
            "name": "Rayuela",
            "author": "Julio Cortázar",
            "isbn": "9788420471570",
            "published_at": date(1963, 6, 28),
            "price": 22.50,
            "stock": 5
        },
        {
            "name": "La casa de los espíritus",
            "author": "Isabel Allende",
            "isbn": "9780525433446",
            "published_at": date(1982, 1, 1),
            "price": 17.99,
            "stock": 9
        },
        {
            "name": "El túnel",
            "author": "Ernesto Sabato",
            "isbn": "9788432217197",
            "published_at": date(1948, 1, 1),
            "price": 13.99,
            "stock": 6
        },
        {
            "name": "Ficciones",
            "author": "Jorge Luis Borges",
            "isbn": "9780802130303",
            "published_at": date(1944, 1, 1),
            "price": 14.99,
            "stock": 11
        },
        {
            "name": "Pedro Páramo",
            "author": "Juan Rulfo",
            "isbn": "9780802133908",
            "published_at": date(1955, 3, 19),
            "price": 13.50,
            "stock": 8
        },
        {
            "name": "Los detectives salvajes",
            "author": "Roberto Bolaño",
            "isbn": "9780374191481",
            "published_at": date(1998, 1, 1),
            "price": 19.99,
            "stock": 4
        },
        {
            "name": "El Aleph",
            "author": "Jorge Luis Borges",
            "isbn": "9780142437889",
            "published_at": date(1949, 1, 1),
            "price": 14.50,
            "stock": 10
        },
        {
            "name": "Como agua para chocolate",
            "author": "Laura Esquivel",
            "isbn": "9780385721233",
            "published_at": date(1989, 1, 1),
            "price": 16.50,
            "stock": 13
        }
    ]
    
    # Create book objects
    books = [Book(**book_data) for book_data in books_data]
    
    # Add all books to the session
    db.add_all(books)
    db.commit()
    
    print(f"Successfully created {len(books)} books in the database!")
    
    # Print summary
    for book in books:
        print(f"  - {book.name} by {book.author} (Stock: {book.stock})")


def main():
    """Main function to run the seed data script"""
    print("Starting database seed...")
    
    # Create tables if they don't exist
    Base.metadata.create_all(bind=engine)
    
    # Create a database session
    db = SessionLocal()
    
    try:
        create_seed_data(db)
    except Exception as e:
        print(f"Error creating seed data: {e}")
        db.rollback()
    finally:
        db.close()
    
    print("Seed process completed!")


if __name__ == "__main__":
    main()
