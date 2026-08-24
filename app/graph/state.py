from typing import TypedDict

class TravelState(TypedDict,total=False):
    #user request
    query: str
    
    #planner info
    source: str | None
    destination: str | None
    days: int | None
    people: int | None
    budget: float | None
    travel_date: str | None
    travel_style: str | None
    
    # Future agents
    flights: list
    trains: list
    weather: dict
    hotels: list

    estimated_budget: dict
    itinerary: str
    recommendation: str