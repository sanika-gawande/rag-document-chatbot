from langchain_ollama import OllamaLLM

# Initialize Phi-3 model
llm = OllamaLLM(
    model="phi3",
    temperature=0.7   # improves response quality
)

# Better prompt for stable output
response = llm.invoke("Give a clear, friendly greeting in one sentence.")

print("Response from Ollama (Phi-3):")
print(response)