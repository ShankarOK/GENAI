from gensim.downloader import load
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

model=load("glove-wiki-gigaword-50")
words = ['football', 'basketball', 'soccer', 'tennis', 'cricket']
vecs=PCA(2).fit_transform([model[x] for x in words])
for (x, y), word in zip(vecs, words):
    plt.scatter(x,y)
    plt.text(x+0.02, y+0.02, word)
plt.show()

for word, similarity in model.most_similar("programming", topn=5):
    print(word, similarity)