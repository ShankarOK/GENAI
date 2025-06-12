from gensim.downloader import load
import random

model = load("glove-wiki-gigaword-50")
iw = "cricket"
words = [w for w, _ in model.most_similar(iw, topn=50)]
random.shuffle(words)
para = f"The topic of {iw} is fascinating, often linked to terms like {', '.join(words)}."
print(para)
