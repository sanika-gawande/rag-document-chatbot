from src.llm_handler import LLMHandler
from src.config import GEMINI_API_KEY

llm = LLMHandler(gemini_key=GEMINI_API_KEY)

response, model = llm.generate_response("What is Artificial Intelligence?")

print("\nModel Used:", model)
print("Response:\n", response)