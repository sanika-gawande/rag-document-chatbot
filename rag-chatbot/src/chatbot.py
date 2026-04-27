from colorama import init, Fore, Style
init()

# Import your modules
from src.document_loader import load_documents, chunk_documents
from src.embeddings import create_vector_store
from src.llm_handler import LLMHandler
from src.rag_pipeline import RAGPipeline
from src.config import GEMINI_API_KEY


class TerminalChatbot:
    def __init__(self, rag_pipeline):
        self.rag_pipeline = rag_pipeline
        self.conversation_history = []

    def print_welcome(self):
        print(f"\n{Fore.CYAN}{'='*60}")
        print("  🤖 RAG-Based Document Chatbot")
        print(f"{'='*60}{Style.RESET_ALL}\n")
        print("Commands: exit | clear | help | status\n")

    def show_help(self):
        print(f"\n{Fore.YELLOW}Available Commands:{Style.RESET_ALL}")
        print("  exit   - Quit chatbot")
        print("  clear  - Clear history")
        print("  help   - Show help")
        print("  status - Show system info\n")

    def show_status(self):
        print(f"\n{Fore.CYAN}System Status:{Style.RESET_ALL}")
        print("✔ RAG Pipeline Loaded")
        print("✔ Vector DB Ready")
        print("✔ LLM Connected\n")

    def run(self):
        self.print_welcome()

        while True:
            try:
                user_input = input(f"{Fore.GREEN}You: {Style.RESET_ALL}").strip()

                # Commands
                if user_input.lower() == "exit":
                    print(f"\n{Fore.CYAN}👋 Goodbye!{Style.RESET_ALL}\n")
                    break

                if user_input.lower() == "clear":
                    self.conversation_history = []
                    print(f"{Fore.YELLOW}✓ Cleared.{Style.RESET_ALL}\n")
                    continue

                if user_input.lower() == "help":
                    self.show_help()
                    continue

                if user_input.lower() == "status":
                    self.show_status()
                    continue

                if not user_input:
                    continue

                # RAG Query
                print(f"\n{Fore.YELLOW}🔍 Searching...{Style.RESET_ALL}", end="\r")

                response, sources, model = self.rag_pipeline.query(user_input)

                print(f"{Fore.BLUE}🤖 Assistant ({model}):{Style.RESET_ALL}")
                print(response, "\n")

                # Show sources
                if sources:
                    print(f"{Fore.MAGENTA}📚 Sources:{Style.RESET_ALL}")
                    for i, doc in enumerate(sources):
                        print(f"{i+1}. {doc.page_content[:100]}...")
                    print()

            except KeyboardInterrupt:
                print(f"\n\n{Fore.CYAN}👋 Goodbye!{Style.RESET_ALL}\n")
                break

            except Exception as e:
                print(f"{Fore.RED}❌ Error: {e}{Style.RESET_ALL}\n")


# 🔥 MAIN ENTRY POINT
if __name__ == "__main__":

    print("🔄 Loading documents...")

    documents = load_documents("./documents")
    chunks = chunk_documents(documents)

    print("🔄 Creating vector database...")
    vector_store = create_vector_store(chunks)

    print("🔄 Initializing LLM...")
    llm_handler = LLMHandler(gemini_key=GEMINI_API_KEY)

    rag_pipeline = RAGPipeline(vector_store, llm_handler)

    print("🚀 Starting chatbot...\n")

    chatbot = TerminalChatbot(rag_pipeline)
    chatbot.run()