import os
import pandas as pd
import networkx as nx
from algoritmos import haversine_km
from clustering import cluster_deliveries

def build_graph(nodes_df, edges_df):
    """Cria o grafo a partir dos nós e arestas."""
    G = nx.Graph()
    for _, r in nodes_df.iterrows():
        G.add_node(int(r['id']), latitude=r['latitude'], longitude=r['longitude'])
    for _, r in edges_df.iterrows():
        G.add_edge(int(r['source']), int(r['target']),
                   distance=r['distance_km'], time=r['time_min'])
    return G

def main():
    print("🚗 Iniciando execução do projeto Rota Inteligente...\n")

    # 1. Carregar dados
    nodes = pd.read_csv('data/nodes.csv')
    edges = pd.read_csv('data/edges.csv')
    deliveries = pd.read_csv('data/deliveries.csv')

    # 2. Construir grafo
    G = build_graph(nodes, edges)
    print(f"Grafo criado com {len(G.nodes())} nós e {len(G.edges())} conexões.\n")

    # 3. Aplicar clustering
    deliveries = cluster_deliveries(deliveries, nodes, k=3)
    print("Clusters formados com sucesso:")
    print(deliveries[['id', 'node_id', 'cluster']])
    print()

    # 4. Calcular distâncias médias por cluster
    dist_medias = []
    for cl in deliveries['cluster'].unique():
        cluster_nodes = deliveries[deliveries['cluster'] == cl]['node_id']
        dist_total = 0
        count = 0
        for i in cluster_nodes:
            for j in cluster_nodes:
                if i < j:
                    dist_total += nx.shortest_path_length(G, source=int(i), target=int(j), weight='distance')
                    count += 1
        dist_media = dist_total / count if count > 0 else 0
        dist_medias.append((cl, dist_media))

    print("Distância média entre entregas por cluster (km):")
    for cl, d in dist_medias:
        print(f" - Cluster {cl}: {d:.2f} km")

    print("\n✅ Execução finalizada com sucesso.")

if __name__ == "__main__":
    main()

