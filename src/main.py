

from matplotlib import pyplot as graph
from sklearn.cluster import AgglomerativeClustering
from sklearn.datasets import make_blobs

n_clusters = 2
colors = ['cyan', 'red']

X, y_gen = make_blobs(n_samples = 200, centers = n_clusters, cluster_std = 2)

for i in range(n_clusters):
    graph.scatter(X[y_gen==i,0], X[y_gen==i,1], c=colors[i])
graph.show()

mdl = AgglomerativeClustering()
y_clustered = mdl.fit_predict(X)

for i in range(n_clusters):
    graph.scatter(X[y_clustered==i,0], X[y_clustered==i,1], c=colors[i])
graph.show()

