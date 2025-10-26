from sqlalchemy import Column, Integer, String, Date, Numeric
from .database import Base


class Book(Base):
    """Book model for storing book information"""
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False, index=True)
    author = Column(String(255), nullable=False, index=True)
    isbn = Column(String(13), unique=True, nullable=False, index=True)
    published_at = Column(Date)
    price = Column(Numeric(6, 2))
    stock = Column(Integer, default=0)
    
    def __repr__(self):
        return f"<Book(id={self.id}, name='{self.name}', author='{self.author}')>"
