from pydantic import BaseModel
from typing import List, Optional


class MovieBase(BaseModel):
    name: str
    date: str
    score: float
    genre: str
    overview: str
    crew: str
    orig_title: str
    status: str
    orig_lang: str
    budget: int
    revenue: int
    country: str


class MovieDetailResponse(MovieBase):
    id: int

    class Config:
        from_attributes = True


class MovieListResponse(BaseModel):
    movies: List[MovieDetailResponse]
    prev_page: Optional[str] = None
    next_page: Optional[str] = None
    total_pages: int
    total_items: int
