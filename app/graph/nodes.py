from agents.planner_agent import PlannerAgent
from agents.flight_agent import FlightAgent
from graph.state import TravelState

planner_agent = PlannerAgent()
flight_agent = FlightAgent()

def planner_node(state: TravelState) -> TravelState:

    print("Planner Node Started")

    query = state["query"]

    result = planner_agent.extract(query)

    return {
        **state,
        "source": result.source,
        "destination": result.destination,
        "days": result.days,
        "people": result.people,
        "budget": result.budget,
        "travel_date": result.travel_date,
        "travel_style": result.travel_style,
    }
    
def flight_node(state: TravelState) -> TravelState:
    
    print("Flight Node Started")
    flights=flight_agent.search(
        source=state["source"],
        destination=state["destination"],
        travel_date=state.get("travel_date")
    )
    
    return {
        **state,
        "flights": flights
    }