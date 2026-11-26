from sklearn.cluster import AffinityPropagation
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import euclidean_distances
import numpy as np

def calculate(data):
    rows=data['references']
    values=[[r[k] for k in ('depth','width','lines')] for r in rows]
    scale=StandardScaler().fit(values)
    vectors=scale.transform(values)
    model=AffinityPropagation(damping=.82, random_state=24, max_iter=400).fit(vectors)
    centers=model.cluster_centers_indices_
    if len(centers)==0 or model.n_iter_>=model.max_iter:
        raise ValueError('代表样传播未收敛')
    query=scale.transform([[data['query'][k] for k in ('depth','width','lines')]])
    cluster=int(euclidean_distances(query,vectors[centers]).argmin())
    return {'exemplar':rows[int(centers[cluster])]['code'],'group_size':int(np.sum(model.labels_==cluster)),
            'clusters':len(centers),'reference_count':len(rows)}
