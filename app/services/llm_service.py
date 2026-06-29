from llm.gemini import llm

class LLMService:
    @staticmethod
    def ask(query:str)->str:
        response=llm.invoke(query)
        return response.content