import itertools as it
from L16_traveling_salesman.travels import *

def brute_salesmas(liste):
    perms = list(it.permutations(range(1, len(liste))))

    paths = []
    for p in perms:
        l = [0] + list(p) + [0]
        print(l)
        paths.append(l)

    best_len = float("inf")
    best_path = -1

    for p in paths:
        counter = 0
        for i in range(len(p) - 1):
            counter += liste[p[i]][p[i + 1]]
        if counter < best_len:
            best_len = counter
            best_path = p

    print(best_len, best_path)