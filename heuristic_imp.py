from sample_generator import generate_random_graph_sample as generator
import random
import sys
from brute_force_imp import vertex_cover_brute


def get_adj(edges, u):
    adj = []
    for edge in edges:
        if u == edge[0] and edge[1] not in adj:
            adj.append(edge[1])
        elif u == edge[1] and edge[0] not in adj:
            adj.append(edge[0])
    return adj


def vertex_cover_heuristic(edges, n_vertices, k):

    visited = (n_vertices+1)*[False]

    for u in range(1, n_vertices+1):
        if not visited[u]:
            for v in get_adj(edges, u):
                if not visited[v]:
                    visited[u] = True
                    visited[v] = True
                    break
    cover = [v for v in range(1, n_vertices+1) if visited[v] == True]
    if len(cover) <= k:
        return [True, cover]
    else:
        return [False, cover]


true = 0
false = 0
for i in range(20):
    size = random.randint(1, 20)
    min = random.randint(1, size)
    graph = generator(size)
    brute = vertex_cover_brute(graph, size, min)
    heuristic = vertex_cover_heuristic(graph, size, min)
    if heuristic[0] == brute[0]:
        true += 1
    else:
        false += 1

# print((true/20)*100)
