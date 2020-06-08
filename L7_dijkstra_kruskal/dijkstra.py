from L7_dijkstra_kruskal.eksempel.adaptable_heap_priority_queue import AdaptableHeapPriorityQueue
from L7_dijkstra_kruskal.eksempel.edge_list_graph import *

infinity = 1000


def dijkstra(g : Graph, s : Vertex):
    Q = AdaptableHeapPriorityQueue()
    dist = {} #dictionary med vertex:distance
    locators = {} #dictionary med vertex:token
    for v in g.vertices(): #initializerer Q og tilføjer alle vertex fra grafen.
        if v == s:
            dist[v] = 0
        else:
            dist[v] = infinity
        loc_token = Q.add(dist[v], v)
        locators[v] = loc_token
    # current = s
    # for edge in g.incident_edges(current):
    #     adjacent = g.opposite(current, edge)
    #     distance = edge.element()
    #     if dist[adjacent] > dist[current] + distance:
    #         dist[adjacent] = dist[current] + distance
    while not Q.is_empty():
        current = Q.remove_min()[1] #remove_min returnerer tuple
        for edge in g.incident_edges(current):
            adjacent = g.opposite(current, edge)
            distance = edge.element()
            if dist[adjacent] > dist[current] + distance:
                dist[adjacent] = dist[current] + distance
    return dist







