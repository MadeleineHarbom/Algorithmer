
from L7_dijkstra_ND.eksempel.edge_list_graph import *


def compare(item1, item2):
    if item1.element() < item2.element():
        return -1
    elif item1.element() > item2.element():
        return 1
    else:
        return 0

class Cluster:

    def __init__(self, node):
        self._root = node
        nodes = [node]

    def parent(self):
        return self._root






def kruskal(g : Graph, v : Vertex ):
    edges = g.sorted_edges()
    for element in edges:
        print(element.element())
    clusters = []
    ver = g.vertices()

    for v in ver:
        clusters.append(Cluster(v))

    for edge in edges:
        if edge.endpoints()[0].





