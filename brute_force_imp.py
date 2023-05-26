import itertools
from sample_generator import generate_random_graph_sample as generator


def vertex_cover_brute(edges, n_vertices, k):
    min_set = None
    min_len = n_vertices + 1

    vertices = [vertex for vertex in range(1, n_vertices + 1)]

    # iterate over all possible sub arrays
    for sub_arr_len in range(1, n_vertices + 1):
        for sub_arr in itertools.combinations(vertices, sub_arr_len):
            # check sub array sub_arr
            flag = True
            for edge in edges:
                if edge[0] not in sub_arr and edge[1] not in sub_arr:
                    flag = False
                    break
            if flag:
                if sub_arr_len < min_len:
                    min_len = sub_arr_len
                    min_set = sub_arr

    if min_len <= k:
        return [True, min_set]
    else:
        return [False, None]
