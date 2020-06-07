# -*- coding: utf-8 -*-
"""
Created on Mon May 25 12:04:12 2020

@author: jhaj
"""

import urllib.request
dist = []

for line in urllib.request.urlopen("https://people.sc.fsu.edu/~jburkardt/datasets/tsp/p01_d.txt"):
    l = line.decode('utf-8').strip().split("        ")
    d = []
    for e in l:
        d.append(int(e))
    dist.append(d)
print(dist)


