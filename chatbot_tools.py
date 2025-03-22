import wikipedia
from duckduckgo_search import DDGS
from datetime import datetime

def search_wikipedia(query):
    """Cerca un argomento su Wikipedia."""
    try:
        summary = wikipedia.summary(query, sentences=2)
        return f"Wikipedia: {summary}"
    except wikipedia.exceptions.PageError:
        return "Wikipedia: Nessuna pagina trovata."
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Wikipedia: Ambiguità, prova con: {', '.join(e.options[:5])}"

def search_duckduckgo(query):
    """Cerca sul web usando DuckDuckGo."""
    with DDGS() as ddgs:
        results = ddgs.text(query, max_results=3)
        return "\n".join([f"{r['title']}: {r['href']}" for r in results])

def save_to_txt(data, filename="research_output.txt"):
    """Salva i dati in un file di testo."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_text = f"--- Research Output ---\nTimestamp: {timestamp}\n\n{data}\n\n"

    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)

    return f"Dati salvati in {filename}"

TOOLS = {
    "wikipedia": search_wikipedia,
    "web": search_duckduckgo,
    "save": save_to_txt,
}
