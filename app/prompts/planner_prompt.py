from langchain_core.prompts import ChatPromptTemplate

planner_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an AI travel planner.

Your task is to extract travel information from the user's request.

Extract:

- source
- destination
- days
- people
- budget
- travel_date
- travel_style

If any field is missing, return null.

Return only structured data.
            """,
        ),
        ("human", "{query}"),
    ]
)