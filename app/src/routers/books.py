from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from .. import crud, schemas
from ..database import get_db

router = APIRouter(
    prefix="/books",
    tags=["Books"]
)

@router.get("/", response_model=List[schemas.BookResponse])
def get_all_books(
        skip: int = 0,
        limit: int = 100,
        db: Session = Depends(get_db)
):
    """Get all books with pagination"""
    books = crud.get_books(db, skip=skip, limit=limit)
    return books


@router.get("/search", response_model=List[schemas.BookResponse])
def search_books(
        name: Optional[str] = None,
        author: Optional[str] = None,
        isbn: Optional[str] = None,
        db: Session = Depends(get_db)
):
    """Search books by name, author, or ISBN"""
    books = crud.search_books(db, name=name, author=author, isbn=isbn)
    return books


@router.get("/{book_id}", response_model=schemas.BookResponse)
def get_book(book_id: int, db: Session = Depends(get_db)):
    """Get a specific book by ID"""
    book = crud.get_book(db, book_id=book_id)
    if not book:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Libro no encontrado"
        )
    return book


@router.post("/{book_id}/buy", response_model=schemas.BookPurchaseResponse)
def buy_book(book_id: int, db: Session = Depends(get_db)):
    """Purchase a book (decrease stock by 1)"""
    book = crud.decrease_book_stock(db, book_id=book_id)

    if not book:
        # Check if book exists
        existing_book = crud.get_book(db, book_id=book_id)
        if not existing_book:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Libro no encontrado"
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Libro agotado"
            )

    return {
        "message": f"Has comprado '{book.name}'",
        "book": book
    }
