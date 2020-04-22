from L8_flow_network.Flow_directed_adjacency_list_graph import *
from L8_flow_network.maximum_flow_network import ford_fulkerson

print('Attempting to greate Max flow graph')

flowgraph = FlowGraph()
s = flowgraph.insert_vertex('s')
v1 = flowgraph.insert_vertex('v1')
v2 = flowgraph.insert_vertex('v2')
v3 = flowgraph.insert_vertex('v3')
v4 = flowgraph.insert_vertex('v4')
t = flowgraph.insert_vertex('t')
flowgraph.insert_edge('s-v1', s, v1, 16)
flowgraph.insert_edge('s-v2', s, v2, 13)
flowgraph.insert_edge('v1-v3', v1, v3, 12)
flowgraph.insert_edge('v2-v4', v2, v4, 14)
flowgraph.insert_edge('v2-v1', v2, v1, 4)
flowgraph.insert_edge('v3-v2', v3, v2, 9)
flowgraph.insert_edge('v4-v3', v4, v3, 7)
flowgraph.insert_edge('v3-t', v3, t, 20)
flowgraph.insert_edge('v4-t', v4, t, 4)

print('Flow graph created')

flowgraph.print_graph(s)
print('About to run')
ford_fulkerson(flowgraph, s, t)
print('Done running')
flowgraph.print_graph(s)

