from L7_dijkstra_kruskal.usable_edge_list_graph import graph, v6
from L7_dijkstra_kruskal.dijkstra import dijkstra
from L7_dijkstra_kruskal.kruskal import kruskal
from L7_dijkstra_kruskal.eksempel.edge_list_graph import *

#dijklist = dijkstra(graph, v6)

#print(dijklist, v6)

#for k in dijklist:
#    print(str(k.element()) + ': ' + str(dijklist[k]))

krugraph = Graph()
a = krugraph.insert_vertex('A')
b = krugraph.insert_vertex('B')
c = krugraph.insert_vertex('C')
d = krugraph.insert_vertex('D')

krugraph.insert_edge(2, a, b)
krugraph.insert_edge(5, a, c)
krugraph.insert_edge(10, a, d)
krugraph.insert_edge(9, b, c)
krugraph.insert_edge(3, b, d)
krugraph.insert_edge(2, c, d)

kruskaltree = kruskal(krugraph)
print('-----------')
for v in kruskaltree:
    print(v.element())

print('-----------')

print('-----------')

print('-----------')

kruskaltree2 = kruskal(graph)
print('-----------')

print('-----------')

print('-----------')
for e in kruskaltree2:
    print(e.element())

