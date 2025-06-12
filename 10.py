import fitz  # PyMuPDF

def extract(file):
    with fitz.open(file) as pdf:
        return "".join(page.get_text() for page in pdf)

def search(query, text):
    query = query.lower()
    lines = text.split('\n')
    results = []
    for line in lines:
        if query in line.lower():
            results.append(line)

    return results or ["No relevant section found."]

def chatbot():
    print("Loading IPC...")
    ipc = extract("IPC.pdf")
    while True:
        query = input("Ask about IPC (type 'exit' to quit): ").strip()
        if query.lower() == "exit":
            print("Goodbye!")
            break
        print("\n".join(search(query, ipc)))
        print("-" * 50)

chatbot()
