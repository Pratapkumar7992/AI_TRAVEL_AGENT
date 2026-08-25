class FlightTool:
    
    def search_flights(self,source:str,destination:str,travel_date:str | None=None):
        flights = [
            {
                "airline": "IndiGo",
                "flight_number": "6E-123",
                "source": source,
                "destination": destination,
                "departure": "06:30",
                "arrival": "08:00",
                "duration": "1h 30m",
                "price": 3200
            },
            {
                "airline": "Air India",
                "flight_number": "AI-456",
                "source": source,
                "destination": destination,
                "departure": "10:15",
                "arrival": "11:50",
                "duration": "1h 35m",
                "price": 3500
            },
            {
                "airline": "IndiGo",
                "flight_number": "6E-789",
                "source": source,
                "destination": destination,
                "departure": "18:20",
                "arrival": "19:50",
                "duration": "1h 30m",
                "price": 2900
            }
        ]

        return flights