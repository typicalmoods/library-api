from sqlalchemy.orm import Session
from typing import List, Optional
from . import models, schemas


def get_book(db: Session, book_id: int) -> Optional[models.Book]:
    """Get a book by ID"""
    return db.query(models.Book).filter(models.Book.id == book_id).first()


def get_books(db: Session, skip: int = 0, limit: int = 100) -> List[models.Book]:
    """Get all books with pagination"""
    return db.query(models.Book).offset(skip).limit(limit).all()


def search_books(
        db: Session,
        name: Optional[str] = None,
        author: Optional[str] = None,
        isbn: Optional[str] = None
) -> List[models.Book]:
    """Search books by name, author, or ISBN"""
    query = db.query(models.Book)

    if name:
        query = query.filter(models.Book.name.ilike(f"%{name}%"))
    if author:
        query = query.filter(models.Book.author.ilike(f"%{author}%"))
    if isbn:
        query = query.filter(models.Book.isbn == isbn)

    return query.order_by(
        models.Book.author.asc(),
        models.Book.name.asc(),
        models.Book.published_at.desc()
    ).all()


def decrease_book_stock(db: Session, book_id: int) -> Optional[models.Book]:
    """Decrease book stock by 1 (for purchase)"""
    db_book = get_book(db, book_id)
    if db_book and db_book.stock > 0:
        db_book.stock -= 1
        db.commit()
        db.refresh(db_book)
        return db_book
    return None
