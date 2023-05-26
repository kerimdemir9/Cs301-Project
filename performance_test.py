from heuristic_imp import vertex_cover_heuristic
from sample_generator import generate_random_graph_sample as generator
import time
import math
import random
import numpy as np
import matplotlib.pyplot as plt


def test(size, k):
    start = time.time()
    graph = generator(size)
    vertex_cover_heuristic(graph, size, k)
    end = time.time()
    return end-start

# with confidence level 95% and N = 100000


def exec(N, size, k):
    tests = []
    for i in range(N):
        tests.append(test(size, k))
    # std = np.std(tests)
    mean = np.mean(tests)
    # sm = std/math.sqrt(N)
    return mean


# graph for input sizes = [5,6,7,8,9,10]


inputSize = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
results = []
for i in range(5, 21):
    results.append(exec(100000, i, random.randint(1, i)))


xlog = np.log(inputSize)
ylog = np.log(results)
plt.loglog(inputSize, results)
# plt.scatter(inputSize, results)
plt.xlabel("log(inputSize)")
plt.ylabel("log(Running time mean)")
plt.show()
