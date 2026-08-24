from langgraph.graph import StateGraph, START , END

from graph.state import TravelState
from graph.nodes import planner_node

def build_travel_graph():
    graph=StateGraph(TravelState)
    
    #add planner node
    graph.add_node("planner",planner_node)
    
    # START → Planner
    graph.add_edge(START,"planner")
    
    # Planner → END
    graph.add_edge("planner",END)
    
    return graph.compile()

travel_graph = build_travel_graph()