''' jmhajek '''
from L7_dijkstra_kruskal.eksempel.adaptable_heap_priority_queue import AdaptableHeapPriorityQueue

a = AdaptableHeapPriorityQueue()
print(a)

p = a.add(1, "Peter")
al = a.add(3, "Allan")
a.update(p, 5, "Peter")
print(a.min())
a.remove_min()
print(a.min())