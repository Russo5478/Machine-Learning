import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

X, y = make_blobs(n_samples=500, centers=5, cluster_std=0.6, random_state=40)

plt.scatter(X[:, 0], X[:, 1])
plt.show()


cluster_numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]
inertia = []
silhouette_scores = []

for k in cluster_numbers:
    kmeans = KMeans(n_clusters=k, random_state=40, n_init=10).fit(X)
    inertia.append(kmeans.inertia_)

    silhouette_avg = silhouette_score(X, kmeans.labels_)
    silhouette_scores.append(silhouette_avg)

    new_point = np.array([[2, 3]])

    # Predict the cluster for the new point
    new_point_cluster = kmeans.predict(X=new_point)

    print(f"Predicted cluster for the new point: {new_point_cluster}, for cluster {k}")


plt.plot(cluster_numbers, inertia, marker='o')
plt.show()

plt.plot(cluster_numbers, silhouette_scores, marker='o')
plt.show()
