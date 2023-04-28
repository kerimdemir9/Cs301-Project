import random

def generate_random_graph_sample(n_vertices):
  edges = []

  for i in range(1, n_vertices + 1):
    for j in range(i + 1, n_vertices + 1):
      rand_int = random.randint(0, 1)
      if rand_int == 1:
        edges.append((i, j))

  return edges

