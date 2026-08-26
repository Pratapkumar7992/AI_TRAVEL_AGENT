class TrainTool:

    def search_trains(
        self,
        source: str,
        destination: str,
        travel_date: str | None = None
    ):

        trains = [
            {
                "train_name": "Vande Bharat Express",
                "train_number": "20704",
                "source": source,
                "destination": destination,
                "departure": "05:30",
                "arrival": "14:00",
                "duration": "8h 30m",
                "price": 1450
            },
            {
                "train_name": "Express Superfast",
                "train_number": "12701",
                "source": source,
                "destination": destination,
                "departure": "16:00",
                "arrival": "06:30",
                "duration": "14h 30m",
                "price": 850
            },
            {
                "train_name": "Garib Rath Express",
                "train_number": "12740",
                "source": source,
                "destination": destination,
                "departure": "20:00",
                "arrival": "09:30",
                "duration": "13h 30m",
                "price": 750
            }
        ]

        return trains