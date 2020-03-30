from L4_grafer_ND.usable_edge_list_graph import graph, v6
from L7_dijkstra_ND.dijkstra import dijkstra

dijklist = dijkstra(graph, v6)

print(dijklist, v6)

for k in dijklist:
    print(str(k.element()) + ': ' + str(dijklist[k]))
