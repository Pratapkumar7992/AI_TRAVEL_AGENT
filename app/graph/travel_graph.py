from langgraph.graph import StateGraph, START , END

from graph.state import TravelState
from graph.nodes import planner_node
from graph.nodes import flight_node

def build_travel_graph():
    graph=StateGraph(TravelState)
    
    #add planner node
    graph.add_node("planner",planner_node)
    graph.add_node("flight",flight_node)
    
    # START → Planner
    graph.add_edge(START,"planner")
    
    # Planner → Flight
    graph.add_edge("planner","flight")
    
    # Flight → END
    graph.add_edge("flight",END)
    
    return graph.compile()

travel_graph = build_travel_graph()