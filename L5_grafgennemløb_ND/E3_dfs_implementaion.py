

#Til adjecency list
def dfs(graph, vertex):
    visited = []
    dfs_helper(graph, vertex, visited)
    return visited

def dfs_helper(graph, vertex, visited):
    if vertex in visited:
        print('backing up')
        return
    else:
        print('new vertex')
        visited.append(vertex)
        for edge in vertex.edges:
            dfs_helper(graph, graph.opposite(vertex, edge), visited)

