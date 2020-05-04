

from matplotlib.colors import XKCD_COLORS
from matplotlib import pyplot as graph
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering
from sklearn.datasets import make_blobs
from sklearn.metrics import accuracy_score


COLORS = list(XKCD_COLORS.values()) # just a big list of colors


def RunSklearn(X, y, mdl):
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
    while True:
        
        option = input("\nHow would you like to cluster?\n 1. sklearn distance threshold\n 2. sklearn n clusters\n 3. scipy dendrogram\n 4. exit\n")
        
        if option == '1':
            scale = 3
            X, y = make_blobs(n_samples = 200*scale, centers = [[1,1], [9*scale,9*scale]], cluster_std = 2*scale)
            mdl = AgglomerativeClustering(n_clusters = None, distance_threshold = 40*scale)
            RunSklearn(X, y, mdl)
            
        elif option == '2':
            n_clusters = 2
            X, y = make_blobs(n_samples = 200, centers = n_clusters, cluster_std = 2)
            mdl = AgglomerativeClustering(n_clusters = n_clusters)
            RunSklearn(X, y, mdl)
            
        elif option == '3':
            X, y = make_blobs(n_samples = 200, centers = 2, cluster_std = 2)
            d = dendrogram(linkage(X, method='ward'))
            graph.show()
            
        elif option == '4':
            break
            
            