from L8_flow_network_ND.directed_adjacency_list_graph import *

class FlowGraph(Graph):
    def __init__(self):
        Graph.__init__(self)


    
graph = Graph()
ns = graph.insert_vertex('s')
nv1 = graph.insert_vertex('v1')
nv2 = graph.insert_vertex('v2')
nv3 = graph.insert_vertex('v3')
nv4 = graph.insert_vertex('v4')
nt = graph.insert_vertex('t')
graph.insert_edge('s - v1', ns, nv1, 16)
graph.insert_edge('s-v2', ns, nv2, 13)
graph.insert_edge('v1-v3', nv1, nv3, 12)
graph.insert_edge('v2-v4', nv2, nv4, 14)
graph.insert_edge('v2-v1', nv2, nv1, 4)
graph.insert_edge('v3-v2', nv3, nv2, 9)
graph.insert_edge('v4-v3', nv4, nv3, 7)
graph.insert_edge('v3-t', nv3, nt, 20)
graph.insert_edge('v4-t', nv4, nt, 4)

print('Graph created, wooo!')

print('Attempting to greate Max flow graph')

flowgraph = FlowGraph()
s = flowgraph.insert_vertex('s')
v1 = flowgraph.insert_vertex('v1')
v2 = flowgraph.insert_vertex('v2')
v3 = flowgraph.insert_vertex('v3')
v4 = flowgraph.insert_vertex('v4')
t = flowgraph.insert_vertex('t')
flowgraph.insert_edge('s - v1', s, v1, 16)
flowgraph.insert_edge('s-v2', s, v2, 13)
flowgraph.insert_edge('v1-v3', v1, v3, 12)
flowgraph.insert_edge('v2-v4', v2, v4, 14)
flowgraph.insert_edge('v2-v1', v2, v1, 4)
flowgraph.insert_edge('v3-v2', v3, v2, 9)
flowgraph.insert_edge('v4-v3', v4, v3, 7)
flowgraph.insert_edge('v3-t', v3, t, 20)
flowgraph.insert_edge('v4-t', v4, t, 4)

print('Flow graph created')