import os
from dotenv import load_dotenv
from crewai import LLM

load_dotenv()

def get_llm():
    return LLM(
        model="groq/llama-3.3-70b-versatile",   # ✅ CrewAI format: provider/model
        api_key="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", # ✅ Your API key from CrewAI
        temperature=0.3,
        max_tokens=4096
    )