from sample_generator import generate_random_graph_sample as generator
import random
import sys
from brute_force_imp import vertex_cover_brute


# def get_adj(edges, u):
#     adj = []
#     for edge in edges:
#         if u == edge[0] and edge[1] not in adj:
#             adj.append(edge[1])
#         elif u == edge[1] and edge[0] not in adj:
#             adj.append(edge[0])
#     return adj


# def vertex_cover_heuristic(edges, n_vertices, k):

#     visited = (n_vertices+1)*[False]

#     for u in range(1, n_vertices+1):
#         if not visited[u]:
#             for v in get_adj(edges, u):
#                 if not visited[v]:
#                     visited[u] = True
#                     visited[v] = True
#                     break
#     cover = [v for v in range(1, n_vertices+1) if visited[v] == True]
#     if len(cover) <= k:
#         return [True, cover]
#     else:
#         return [False, cover]

def remove(edges, u, v):
    newEdges = []
    for edge in edges:
        if (u not in edge) and (v not in edge):
            newEdges.append(edge)
    return newEdges


def vertex_cover_heuristic(edges):
    vertexCover = []
    UC = edges
    while len(UC) > 0:
        CE = UC[random.randint(0, len(UC)-1)]
        vertexCover.append(CE[0])
        vertexCover.append(CE[1])
        UC = remove(UC, CE[0], CE[1])
    return vertexCover
