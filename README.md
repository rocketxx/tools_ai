# Chatbot con Strumenti Intelligenti

Questo progetto implementa un chatbot intelligente che può eseguire diverse azioni utilizzando strumenti esterni. Ad esempio, può rispondere a domande, cercare informazioni su Wikipedia, cercare nel web con DuckDuckGo e salvare risultati su un file di testo. Il bot usa **Ollama** per la generazione del linguaggio naturale e integra diversi strumenti per eseguire ricerche e operazioni.

## Come configurare il progetto

### 1. Crea un ambiente virtuale

Per prima cosa, è necessario creare un ambiente virtuale per gestire le dipendenze del progetto:

```bash
python -m venv venv
```

### 2. Attiva l'ambiente virtuale

Una volta creato l'ambiente virtuale, attivalo con il comando appropriato per il tuo sistema operativo:

#### Su Windows:

```bash
.\env\Scripts\ctivate
```

#### Su macOS/Linux:

```bash
source venv/bin/activate
```

### 3. Installa le dipendenze

Dopo aver attivato l'ambiente virtuale, installa le dipendenze richieste per il progetto. Esegui il comando:

```bash
pip install -r .
equirements.txt
```

Questo comando installerà tutte le librerie necessarie, incluse quelle per l'interazione con Wikipedia, DuckDuckGo, e Ollama.

### 4. Configura il progetto

Il progetto si basa su `Ollama` (un modello di linguaggio) e alcuni strumenti esterni per completare le operazioni. Assicurati di avere una chiave API per Ollama o il suo client di esecuzione se necessario.

Inoltre, puoi aggiungere qualsiasi altro strumento (come quelli per la ricerca su Wikipedia o per il salvataggio dei risultati).

### 5. Esegui il bot

Per avviare il chatbot, esegui il file Python principale con il comando:

```bash
python main.py
```

Quando esegui il bot, ti verrà chiesto di inserire una domanda o una richiesta. Il bot deciderà se rispondere direttamente o utilizzare uno degli strumenti (come la ricerca su Wikipedia o DuckDuckGo) per soddisfare la richiesta.

### 6. Struttura del codice

Il file `main.py` gestisce la logica principale del bot. Esso utilizza `Ollama` per generare risposte e invoca strumenti esterni per cercare informazioni o salvare risultati. La logica è la seguente:

1. **Sistema**: Il bot può rispondere direttamente o usare strumenti esterni (Wikipedia, DuckDuckGo, o il salvataggio su file).
2. **Richiesta dell'utente**: Quando l'utente fa una richiesta, il bot decide se rispondere direttamente o utilizzare uno degli strumenti.
3. **Strumenti**:
   - **Wikipedia**: Cerca informazioni su Wikipedia.
   - **Web (DuckDuckGo)**: Effettua una ricerca su DuckDuckGo.
   - **Save**: Salva i risultati in un file di testo.

### 7. Funzionamento interno

Il bot usa il modello `Ollama` per decidere se rispondere direttamente o utilizzare uno strumento esterno in base alla richiesta dell'utente. La risposta viene quindi formattata nel formato JSON per indicare quale strumento utilizzare e quale query passare ad esso.

Ecco un esempio di interazione con il bot:

```
🤖 Chatbot con Tool Intelligenti - Digita 'exit' per uscire.

👤 Tu: Chi è Leonardo da Vinci?
🤖 {"action": "wikipedia", "query": "Leonardo da Vinci"}
```

Il bot effettuerà una ricerca su Wikipedia e restituirà una risposta sintetica basata sulla pagina di Wikipedia di Leonardo da Vinci.

### 8. Requisiti

- **Python 3.x**
- **Ollama** (per il modello di linguaggio)
- **Wikipedia-API** (per la ricerca su Wikipedia)
- **DuckDuckGoSearch** (per la ricerca web)
- **Altri strumenti di utilità** (come la funzione di salvataggio su file)

### 9. Risoluzione dei problemi

Se incontri errori durante l'esecuzione del bot, ecco alcuni suggerimenti:

- Verifica che tutte le dipendenze siano correttamente installate.
- Assicurati che il tuo ambiente virtuale sia attivo quando esegui il bot.
- Se hai problemi con `Ollama`, assicurati di avere la versione corretta del client e una chiave API valida (se necessaria).
- Per la ricerca su Wikipedia, verifica che la libreria `wikipedia-api` sia correttamente configurata.

---

### 10. Contributi

Se desideri contribuire a questo progetto, sentiti libero di fare un fork del repository, apportare modifiche e inviare una pull request.

---

**Autore**: RocketXX
**Licenza**: MIT
