from sklearn.cluster import KMeans
import numpy as np
import pandas as pd

def cluster_deliveries(deliveries_df, nodes_df, k=3):
    """
    Aplica K-Means para agrupar entregas em zonas próximas.
    Retorna o dataframe de entregas com a coluna 'cluster' adicionada.
    """
    coords = []
    for _, row in deliveries_df.iterrows():
        node = nodes_df[nodes_df['id'] == row['node_id']].iloc[0]
        coords.append([node['latitude'], node['longitude']])
    coords = np.array(coords)
    
    # Define número de clusters máximo igual ao número de entregas
    kmeans = KMeans(n_clusters=min(k, len(coords)), random_state=0).fit(coords)
    deliveries_df['cluster'] = kmeans.labels_
    
    return deliveries_df

