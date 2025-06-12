from gensim.models import Word2Vec

corpus=[
    "The patient was prescribed antibiotics to treat the infection.".split(),
    "The court ruled in favor of the defendant after reviewing the evidence.".split(),
    "Diagnosis of diabetes mellitus requires specific blood tests.".split(),
    "The legal contract must be signed in the presence of a witness.".split(),
    "Symptoms of the disease include fever, cough, and fatigue.".split(),
    "The patient was advised to follow a strict diet and exercise regimen.".split(),
    "The judge delivered a verdict based on the presented facts.".split(),
    "Early detection of cancer can significantly improve treatment outcomes.".split(),
    "The lawyer prepared the case meticulously for the upcoming trial.".split(),
]

model= Word2Vec(corpus, vector_size=50, epochs=10, min_count=1)

for word in ["patient", "court"]:
    print(f"Similar words to '{word}':")
    for word, similarity in model.wv.most_similar(word, topn=5):
        print(f"{word}: {similarity}")
    print()



































# from gensim.models import Word2Vec

# # Training data
# corpus = [
#     "The patient was prescribed antibiotics to treat the infection.".split(),
#     "The court ruled in favor of the defendant after reviewing the evidence.".split(),
#     "Diagnosis of diabetes mellitus requires specific blood tests.".split(),
#     "The legal contract must be signed in the presence of a witness.".split(),
#     "Symptoms of the disease include fever, cough, and fatigue.".split(),
# ]

# # Train Word2Vec model
# model = Word2Vec(corpus, vector_size=50, epochs=10, min_count=1)

# # Show similar words
# for word in ["patient", "court"]:
#     print(f"Similar to '{word}':")
#     for w, s in model.wv.most_similar(word, topn=5):
#         print(w, s)
#     print()

