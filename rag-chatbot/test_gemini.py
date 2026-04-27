from google import genai
from langchain_ollama import OllamaLLM
import os

def get_response(prompt):
    try:
        client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        return response.text
    except:
        llm = OllamaLLM(model="phi3")
        return llm.invoke(prompt)

print(get_response("Say hello"))