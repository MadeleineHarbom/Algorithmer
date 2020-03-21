from L4_grafer_ND.usable_adjacency_list_grapf import graph, v15, v38, v123, unconnected_graph, v42
from L5_grafgennemløb_ND.E1_dfs_recursion_iterator import dfs_iterator
from L5_grafgennemløb_ND.E2_connections import is_graph_connected, is_verticies_adjacent, are_verticies_connected
from L5_grafgennemløb_ND.E3_dfs_implementaion import dfs
from L5_grafgennemløb_ND.E4_BFS_ND import bfs, bfs_distance



print('Implement dfsVisit using recursion; iteratorDFS will return the iterator. (See the algorithm in the graph note)')
iterator = dfs_iterator().iterator_dfs(graph, v15)

for x in iterator:
    print(x)

print('Implement a method that takes a graph as a parameter and determines whether or not the graph is connected.')

print(is_graph_connected(graph, v15))


print('Implement a method that takes a graph and two vertices as parameters and determines whether or not there is a path from one to the other.')
print('Should be adjacent')
print(is_verticies_adjacent(v15, v38))
print('Shouldnt be adjacent')
print(is_verticies_adjacent(v15, v123))
print('Should be conencted')
print(are_verticies_connected(graph, v15, v123))
print('Shouldnt be conencted')
print(are_verticies_connected(unconnected_graph, v15, v42))

print('Implement the DFS from slide 7, marking all labels as discovery edges or back edges.')
print(dfs(graph, v15))

print('BFS')
print(len(bfs(graph, v15)))

print('Modify Breadth-first in a way that returns the distance between the starting vertex and every vertex in the (connected) graph.')
bfs_dictionary = bfs_distance(graph, v15)

for key in bfs_dictionary:
    print(key.element())
    print(bfs_dictionary[key])



