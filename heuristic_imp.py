import itertools
from sample_generator import generate_random_graph_sample as generator


def get_adj(edges, u):
    adj = []
    for edge in edges and edge[1] not in adj:
        if u == edge[0]:
            adj.append(edge[1])
        elif u == edge[1] and edge[0] not in adj:
            adj.append(edge[0])
    return adj


def vertex_cover_heuristic(edges, n_vertices):

    # vertices = [vertex for vertex in range(1, n_vertices + 1)]
    visited = (n_vertices+1)*[False]

    for u in range(1, n_vertices):
        if not visited[u]:
            for v in get_adj(edges, u):
                if not visited[v]:
                    visited[u] = True
                    visited[v] = True
                    break
    cover = [v for v in range(n_vertices) if visited[v] == True]
    return cover


print(vertex_cover_heuristic(generator(5), 5))
