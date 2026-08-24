from app.graph.travel_graph import travel_graph


def test_planner_graph():

    initial_state = {
        "query": "Plan a 5 day trip from Hyderabad to Goa for 2 people with a budget of 30000"
    }

    result = travel_graph.invoke(initial_state)

    print(result)

    assert result["source"] == "Hyderabad"
    assert result["destination"] == "Goa"