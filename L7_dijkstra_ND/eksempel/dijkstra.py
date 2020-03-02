from L7_dijkstra_ND.eksempel.edge_list_graph import *

from L7_dijkstra_ND.eksempel.adaptable_heap_priority_queue import AdaptableHeapPriorityQueue

infinity = 1000

def dijkstra(g, s):
    q = AdaptableHeapPriorityQueue()
    dist = {}
    locators = {}
    for v in g.vertices():
        if v == s:
            dist[v] = 0
        else:
            dist[v] = infinity
        l = q.add(dist[v], v)
        locators[v] = l
        