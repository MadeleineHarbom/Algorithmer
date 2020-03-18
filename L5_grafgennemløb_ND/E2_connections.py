from L4_grafer_ND.E2_find_max_adjecency import populate_visited_recursive


def is_graph_connected(graph, vertex):
    visited = []
    populate_visited_recursive(visited, vertex)
    if len(visited) == graph.num_vertices():
        return True
    else:
        return False


def is_verticies_connected(vertex1, vertex2):
    for edge in vertex1.edges:
        if vertex1 in edge.endpoints() and vertex2 in edge.endpoints():
            return True
    return False
