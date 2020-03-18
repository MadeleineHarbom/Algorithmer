from L4_grafer_ND.adjacency_list_graph import *

graph = Graph()

v15 = graph.insert_vertex(15)
v38 = graph.insert_vertex(38)
e10 = graph.insert_edge(10, v15, v38)

v123 = graph.insert_vertex(123)
e55 = graph.insert_edge(55, v38, v123)

v66 = graph.insert_vertex(66)
e76 = graph.insert_edge(76, v66, v123)

v6 = graph.insert_vertex(6)
e8 = graph.insert_edge(8, v6, v66)
e23 = graph.insert_edge(23, v6, v15)

e90 = graph.insert_edge(90, v66, v15)
e7 = graph.insert_edge(7, v6, v123)
e2 = graph.insert_edge(2, v66, v38)


unconnected_graph = Graph()
v15 = unconnected_graph.insert_vertex(15)
v38 = unconnected_graph.insert_vertex(38)
e10 = unconnected_graph.insert_edge(10, v15, v38)

v123 = unconnected_graph.insert_vertex(123)
e55 = unconnected_graph.insert_edge(55, v38, v123)

v66 = unconnected_graph.insert_vertex(66)
e76 = unconnected_graph.insert_edge(76, v66, v123)

v6 = unconnected_graph.insert_vertex(6)
e8 = unconnected_graph.insert_edge(8, v6, v66)
e23 = unconnected_graph.insert_edge(23, v6, v15)

e90 = unconnected_graph.insert_edge(90, v66, v15)
e7 = unconnected_graph.insert_edge(7, v6, v123)
e2 = unconnected_graph.insert_edge(2, v66, v38)

v42 = unconnected_graph.insert_vertex(42)
v69 = unconnected_graph.insert_vertex(69)
e19 = unconnected_graph.insert_edge(78, v42, v69)
