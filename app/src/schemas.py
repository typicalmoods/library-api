from pydantic import BaseModel, Field, ConfigDict
from datetime import date
from typing import Optional


class BookBase(BaseModel):
    """Base schema for Book with common attributes"""
    name: str = Field(..., min_length=1, max_length=255, description="Book title")
    author: str = Field(..., min_length=1, max_length=255, description="Book author")
    isbn: str = Field(..., min_length=10, max_length=13, description="ISBN code")
    published_at: Optional[date] = Field(None, description="Publication date")
    price: Optional[float] = Field(None, ge=0, description="Book price")
    stock: Optional[int] = Field(0, ge=0, description="Available stock")


class BookResponse(BookBase):
    """Schema for book response with ID"""
    id: int
    
    model_config = ConfigDict(from_attributes=True)


class BookPurchaseResponse(BaseModel):
    """Schema for book purchase response"""
    message: str
    book: BookResponse
    
    model_config = ConfigDict(from_attributes=True)
