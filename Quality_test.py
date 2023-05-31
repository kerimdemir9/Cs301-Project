from heuristic_imp import vertex_cover_heuristic
from sample_generator import generate_random_graph_sample as generator
from brute_force_imp import vertex_cover_brute
import pandas as pd
import random
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


def qualityTest(inputSize):
    res = {
        "true": 0,
        "false": 0
    }
    for i in range(1000):
        graph = generator(inputSize)
        k = random.randint(1, inputSize)
        brute = vertex_cover_brute(graph, inputSize, k)
        heuristic = vertex_cover_heuristic(graph, inputSize, k)
        if heuristic[0] == brute[0]:
            res["true"] += 1
        else:
            res["false"] += 1
    return res


# test one inputSize for 10000 times

inputSize = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
results = []

for i in range(5, 18):
    results.append(qualityTest(i))
    print(results)

true = []
false = []
for l in results:
    true.append(l["true"])
    false.append(l["false"])


barWidth = 0.25
fig = plt.subplots(figsize=(12, 8))
br1 = np.arange(len(true))
br2 = [x + barWidth for x in br1]
plt.bar(br1, true, width=barWidth, label='True')
plt.bar(br2, false, width=barWidth, label='False')
plt.xlabel('inputSize')
plt.ylabel('Correctness')
plt.xticks([r + barWidth/2 for r in range(len(true))], inputSize)
plt.legend()
plt.show()
