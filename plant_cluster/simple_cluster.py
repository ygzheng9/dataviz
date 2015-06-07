# imports needed for the following examples
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import scipy.spatial.distance as distance
import scipy.cluster.hierarchy as hierarchy

a = [[1,2,3], [2,4,6], [1000, 2000, 3000], [2,3,4], [4,5,6], [100,200,300],
     [101,201,310], [150, 220, 301], [1500, 1500, 1500]]
idx = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
columns = ['po', 'cnt', 'amt']
df = pd.DataFrame(a, index=idx, columns=columns)

n = df.shape[0]
k = 4

# condensed distance is enough
d = hierarchy.distance.pdist(df)

# no need for squared distance
# rtn_square = distance.squareform(d)

Z = hierarchy.linkage(d, method='single')
T = hierarchy.fcluster(Z, k, 'maxclust')

# order for the cluster, no need for plot
# headmap_order = hierarchy.leaves_list(link)
# df['cluster_order'] = T
# df.sort('cluster_order')

# calculate labels
labels = list('' for i in range(n))
for i in range(n):
    labels[i] = str(T[i]) + '-' + df.index[i]

# log2 to change the distance for better plot
for line in Z:
    line[2] = np.log(line[2])

# calculate color threshold
ct = Z[-(k-1), 2]

# plot
P = hierarchy.dendrogram(Z, labels=labels, color_threshold=ct)

plt.show()
