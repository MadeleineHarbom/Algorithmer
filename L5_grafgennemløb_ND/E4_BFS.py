
#adjecendcy list graph
def bfs(graph, startnode):
    discovered = [startnode]
    bfs_helper(graph, startnode, discovered)
    return discovered

def bfs_helper(graph, node, discorvered):
    level = [node]
    while len(level) > 0:
        next_level = []
        for vertex in level:
            for edge in graph.incident_edges(vertex):
                opposite_vertex = graph.opposite(vertex, edge)
                if opposite_vertex not in discorvered:
                    discorvered.append(opposite_vertex)
                    next_level.append(opposite_vertex)
        level = next_level


def bfs_distance(graph, startnode):
    discovered = {startnode: 0}
    bfs_distance_helper(graph, startnode, discovered)
    return discovered


def bfs_distance_helper(graph, node, discorvered):
    level = [node]
    while len(level) > 0:
        next_level = []
        for vertex in level:
            for edge in graph.incident_edges(vertex):
                opposite_vertex = graph.opposite(vertex, edge)
                if opposite_vertex not in discorvered:
                    discorvered[opposite_vertex] = discorvered[vertex] + edge.element()
                    next_level.append(opposite_vertex)
        level = next_level


