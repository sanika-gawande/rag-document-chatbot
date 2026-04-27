import google.generativeai as genai

from langchain_ollama import OllamaLLM
import time


class LLMHandler:
    def __init__(self, gemini_key, ollama_model="phi3"):
        self.gemini_key = gemini_key
        self.ollama_model = ollama_model
        self.setup_gemini()
        self.setup_ollama()

    def setup_gemini(self):
        """Initialize Gemini API"""
        genai.configure(api_key=self.gemini_key)
        self.gemini = genai.GenerativeModel("gemini-1.5-flash")

    def setup_ollama(self):
        """Initialize Ollama"""
        self.ollama = OllamaLLM(model=self.ollama_model)

    def generate_response(self, prompt, use_fallback=False):
        """Generate response with automatic fallback"""

        # Try Gemini first
        if not use_fallback:
            try:
                response = self.gemini.generate_content(prompt)
                return response.text, "gemini"

            except Exception as e:
                print(f"⚠️ Gemini failed: {e}")
                print("🔄 Switching to Ollama...")
                time.sleep(1)

        # Fallback → Ollama
        try:
            response = self.ollama.invoke(prompt)
            return response, "ollama"

        except Exception as e:
            return f"Error: Both LLMs failed → {e}", "error"