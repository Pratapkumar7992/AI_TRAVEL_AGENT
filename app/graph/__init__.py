from typing import TypedDict,Optional

class TravelState(TypedDict):
    query:str
    
    source:Optional[str]
    destination:Optional[str]
    days:Optional[int]
    people:Optional[int]
    budget:Optional[int]
    travel_date:Optional[str]
    travel_style:Optional[str]
    
    flight:Optional[list]
    train:Optional[list]
    weather:Optional[dict]
    hotel:Optional[list]
    estimated_budget:Optional[dict]
    itinerary:Optional[str]
    recommendations:Optional[str]