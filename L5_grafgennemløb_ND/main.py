from L4_grafer_ND.usable_adjacency_list_grapf import graph, v15, v38, v123
from L5_grafgennemløb_ND.E1_dfs_recursion_iterator import dfs_iterator
from L5_grafgennemløb_ND.E2_connections import is_graph_connected, is_verticies_connected


print('Implement dfsVisit using recursion; iteratorDFS will return the iterator. (See the algorithm in the graph note)')
iterator = dfs_iterator().iterator_dfs(graph, v15)

for x in iterator:
    print(x)

print('Implement a method that takes a graph as a parameter and determines whether or not the graph is connected.')

print(is_graph_connected(graph, v15))


print('Implement a method that takes a graph and two vertices as parameters and determines whether or not there is a path from one to the other.')
print(is_verticies_connected(v15, v38))
print(is_verticies_connected(v15, v123))

print('Implement the DFS from slide 7, marking all labels as discovery edges or back edges.')