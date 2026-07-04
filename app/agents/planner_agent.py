from app.llm.gemini import llm
from app.prompts.planner_prompt import planner_prompt
from app.schemas.travel_request import TravelRequest


class PlannerAgent:

    def extract(self, query: str) -> TravelRequest:
        structured_llm = llm.with_structured_output(TravelRequest)

        chain = planner_prompt | structured_llm

        return chain.invoke({"query": query})