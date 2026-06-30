from typing import Optional

from pydantic import BaseModel


class TravelRequest(BaseModel):
    source: Optional[str] = None
    destination: Optional[str] = None
    days: Optional[int] = None
    people: Optional[int] = None
    budget: Optional[int] = None
    travel_date: Optional[str] = None
    travel_style: Optional[str] = None