from tools.flight_tool import FlightTool

class FlightAgent:
    
    def __init__(self):
        self.flight_tool = FlightTool()
        
    def search(self,source:str,destination:str,travel_date:str | None=None):
        return self.flight_tool.search_flights(source,destination,travel_date)