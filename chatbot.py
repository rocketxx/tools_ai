import ollama
from chatbot_tools import TOOLS

SYSTEM_PROMPT = """
Sei un assistente AI con accesso a strumenti specializzati.
Quando l'utente fa una richiesta, decidi se è meglio:
1. Rispondere direttamente
2. Usare uno strumento esterno

Rispondi nel formato:
{"action": "nome_tool", "query": "testo da passare al tool"}
oppure
{"action": "chat", "response": "risposta normale"}

Gli strumenti disponibili sono:
- "wikipedia" per cercare su Wikipedia
- "web" per cercare su DuckDuckGo
- "save" per salvare un testo

Se la richiesta non richiede un tool, rispondi direttamente.
"""

def process_request(user_input):
    """Usa Ollama per decidere se usare un tool o rispondere normalmente."""
    response = ollama.chat(
        model="mistral",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_input},
        ]
    )

    try:
        result = eval(response["message"]["content"])  # Converte il JSON in Python dict
        if result["action"] == "chat":
            return result["response"]
        elif result["action"] in TOOLS: #controlla che esiste il tool
            return TOOLS[result["action"]](result["query"])  #in questo caso richiama il tool. ACTION sarà ad esempio "search_duckduckgo" e query ciò che deve passare alla funzione: search_duckduckgo("News about AI") 
        else:
            return "⚠️ Tool non riconosciuto."
    except Exception as e:
        return f"Errore nell'elaborazione della risposta: {e}"

def chat_with_ollama():
    print("🤖 Chatbot con Tool Intelligenti - Digita 'exit' per uscire.\n")
    
    while True:
        user_input = input("👤 Tu: ")
        if user_input.lower() == "exit":
            print("👋 Arrivederci!")
            break

        response = process_request(user_input)
        print(f"🤖 {response}\n")

if __name__ == "__main__":
    chat_with_ollama()
