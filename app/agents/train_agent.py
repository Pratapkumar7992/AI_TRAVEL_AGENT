from tools.train_tool import TrainTool

class TrainAgent:
    
    def __init__(self):
        self.train_tool = TrainTool()
        
    def search(self,source:str,destination:str,travel_date:str | None=None):
        return self.train_tool.search_trains(source,destination,travel_date)