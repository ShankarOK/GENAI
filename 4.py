from gensim.downloader import load
from transformers import pipeline

model = load("glove-wiki-gigaword-50")

# Enrich the input prompt with similar words
def enrich(prompt):
    sw = prompt.split()
    for word in prompt.split():
            sw += [w for w, _ in model.most_similar(word, topn=3)]
    return " ".join(sw)

op = "lung cancer"
ep = enrich(op)

print("Original:", op)
print("Enriched:", ep)

gen = pipeline("text-generation", model="gpt2")

print("\nOriginal Response:\n")
print(gen(op, max_length=100)[0]["generated_text"])

print("\nEnriched Response:\n")
print(gen(ep)[0]["generated_text"])
