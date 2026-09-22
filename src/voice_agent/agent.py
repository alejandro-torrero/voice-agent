from livekit.agents import Agent
from livekit.plugins import openai


class Assistant(Agent):
    
    def __init__(self,system_prompt: str) -> None:
        super().__init__(            
            llm=openai.LLM(model="gpt-4.1-mini"),
            instructions=system_prompt
        )