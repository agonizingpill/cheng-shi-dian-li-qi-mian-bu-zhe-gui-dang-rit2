from sklearn.cluster import AffinityPropagation
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import euclidean_distances
import numpy as np

FEATURES = ('depth', 'width', 'lines')

def fit(rows):
    values=[[r[k] for k in FEATURES] for r in rows]
    scale=StandardScaler().fit(values)
    vectors=scale.transform(values)
    model=AffinityPropagation(damping=.82, random_state=24, max_iter=400).fit(vectors)
    centers=model.cluster_centers_indices_
    if len(centers)==0 or model.n_iter_>=model.max_iter:
        raise ValueError('代表样传播未收敛')
    return scale, vectors, model, centers

def exemplar_of(fitted, rows, sample):
    scale, vectors, model, centers = fitted
    query=scale.transform([[sample[k] for k in FEATURES]])
    cluster=int(euclidean_distances(query,vectors[centers]).argmin())
    return rows[int(centers[cluster])]['code']

def calculate(data):
    rows=data['references']
    fitted=fit(rows)
    scale, vectors, model, centers = fitted
    query=scale.transform([[data['query'][k] for k in FEATURES]])
    cluster=int(euclidean_distances(query,vectors[centers]).argmin())
    return {'exemplar':rows[int(centers[cluster])]['code'],'group_size':int(np.sum(model.labels_==cluster)),
            'clusters':len(centers),'reference_count':len(rows)}

def calculate_trial(data):
    rows=data['fit']
    fitted=fit(rows)
    base_rows=data.get('baseline_fit') or None
    base=fit(base_rows) if base_rows else None
    report=[]
    for sample in data['holdout']:
        exemplar=exemplar_of(fitted, rows, sample)
        other=exemplar_of(base, base_rows, sample) if base else None
        report.append({'sample':sample['code'],'exemplar':exemplar,'baseline_exemplar':other,
                       'agree':(exemplar==other) if other is not None else None})
    agreed=sum(1 for row in report if row['agree'])
    return {'rows':report,'fit_count':len(rows),'holdout_count':len(report),
            'compared':base is not None,'agree':agreed if base else None,
            'disagree':(len(report)-agreed) if base else None}
