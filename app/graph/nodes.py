from agents.planner_agent import PlannerAgent
from graph.state import TravelState

planner_agent = PlannerAgent()

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