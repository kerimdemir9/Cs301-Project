from sample_generator import generate_random_graph_sample as generator
import random


def remove(edges, u, v):
    newEdges = []
    for edge in edges:
        if (u not in edge) and (v not in edge):
            newEdges.append(edge)
    return newEdges


def vertex_cover_heuristic(edges, n_vertices, k):
    if k < 0 or k > n_vertices or n_vertices == 0 or edges == []:
        return [False, []]
    vertexCover = []
    UC = edges
    while len(UC) > 0:
        CE = UC[random.randint(0, len(UC)-1)]
        vertexCover.append(CE[0])
        vertexCover.append(CE[1])
        UC = remove(UC, CE[0], CE[1])

    if len(vertexCover) <= k:
        return [True, vertexCover]
    else:
        return [False, vertexCover]
