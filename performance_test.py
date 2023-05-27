from heuristic_imp import vertex_cover_heuristic
from sample_generator import generate_random_graph_sample as generator
import time
import math
import random
import numpy as np
import matplotlib.pyplot as plt


def test(size):
    start = time.time()
    graph = generator(size)
    vertex_cover_heuristic(graph)
    end = time.time()
    return end-start


def exec(N, size):
    tests = []
    for i in range(N):
        tests.append(test(size))
    # std = np.std(tests)
    mean = np.mean(tests)
    # sm = std/math.sqrt(N)
    # t = 1.645
    return mean

# graph for input sizes = [5,6,7,8,9,10]


print(exec(100000, 10))
inputSize = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
results = []
for i in range(5, 21):
    results.append(exec(100000, i))


xlog = np.log(inputSize)
ylog = np.log(results)
slope, intercept = np.polyfit(xlog, ylog, 1)
plt.loglog(inputSize, results)
print(slope)
# plt.scatter(inputSize, results)
plt.xlabel("log(inputSize)")
plt.ylabel("log(Running time mean)")
plt.show()
