from L4_grafer_ND.usable_adjacency_list_grapf  import graph, v15
from L5_grafgennemløb_ND.E1_dfs_recursion_iterator import dfs_iterator


print('Implement dfsVisit using recursion; iteratorDFS will return the iterator. (See the algorithm in the graph note)')
iterator = dfs_iterator().iterator_dfs(graph, v15)

for x in iterator:
    print(x)

print('Implement a method that takes a graph as a parameter and determines whether or not the graph is connected.')

print('Implement a method that takes a graph and two vertices as parameters and determines whether or not there is a path from one to the other.')