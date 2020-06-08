from typing import Dict

from L7_dijkstra_kruskal.eksempel.edge_list_graph import *
from L7_dijkstra_kruskal.eksempel.adaptable_heap_priority_queue import AdaptableHeapPriorityQueue


def compare(item1, item2):
    if item1.element() < item2.element():
        return -1
    elif item1.element() > item2.element():
        return 1
    else:
        return 0

class Cluster:

    class Position:

        def __init__(self, container, element):
            self._container = container
            self._element = element
            self._size = 1
            self._parent = self

        def element(self):
            return self._element

    def make_grp(self, element):
        return self.Position(self, element) #laver en position og sætter self (cluster) som container


    def find(self, position): #kig på mig, nok ikke parent, position?
        if position._parent != position:
            position._parent = self.find(position._parent) #looper til fanil-parent er funet
        return position._parent


    def union(self, element1, element2):
        a = self.find(element1)
        b = self.find(element2)
        if a is not b:
            if a._size > b._size:
                b._parent = a
                a._size = b._size
            else:
                a._parent = b
                b._size += a._size




def kruskal(g : Graph):
    q = AdaptableHeapPriorityQueue()
    position: Dict[Vertex, Cluster.Position] = {}
    forest = Cluster()

    for e in g.edges():
        print(e.element())
        q.add(e.element(), e)
    clusters = []
    ver = g.vertices()
    num_v = 0
    for ve in ver:
        position[ve] = forest.make_grp(ve)
        num_v += 1


    minimum_spanning_tree = [] #tree
    while not q.is_empty() and len(minimum_spanning_tree) < num_v:
        weight, edge = q.remove_min()
        v1, v2 = edge.endpoints()

        a = forest.find(position[v1])
        b = forest.find(position[v2])
        if a != b:
            minimum_spanning_tree.append(edge)
            forest.union(a, b)

    return minimum_spanning_tree