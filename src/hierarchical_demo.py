

from matplotlib.colors import XKCD_COLORS
from matplotlib import pyplot as graph
from sklearn.cluster import AgglomerativeClustering
from sklearn.datasets import make_blobs
from sklearn.metrics import accuracy_score


COLORS = list(XKCD_COLORS.values()) # just a big list of colors


def Run(X, y, mdl):
    """
        BRIEF  Show the graph before and after clustering
    """
    for i in range(len(X)):
        graph.scatter(X[i,0], X[i,1], c=COLORS[y[i]])
    graph.show()

    y_clustered = mdl.fit_predict(X)

    for i in range(len(X)):
        graph.scatter(X[i,0], X[i,1], c=COLORS[y_clustered[i]])
    graph.show()
    
    
if __name__ == '__main__':
    """
        BRIEF  Main execution
    """
    proceed = True
    while proceed:
    
        option = input("\nHow would you like to cluster?\n1. Distance threshold\n2. Hard-coded number of clusters\n")
        
        if option == '1':
            scale = 3
            centers = [1,1], [9*scale,9*scale]
            X, y = make_blobs(n_samples = 200*scale, centers = centers, cluster_std = 2*scale)
            mdl = AgglomerativeClustering(n_clusters = None, distance_threshold = 40*scale)
            Run(X, y, mdl)
            
        elif option == '2':
            centers = 2
            X, y = make_blobs(n_samples = 200, centers = centers, cluster_std = 2)
            mdl = AgglomerativeClustering(n_clusters = centers)
            Run(X, y, mdl)
            
            