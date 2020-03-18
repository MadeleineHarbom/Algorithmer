from L4_grafer_ND.usable_adjacency_list_grapf import graph, v15





def find_max(first):
    visited = []

    populate_visited_recursive(visited, first)
    maxx = -90000
    for vev in visited:
        if vev.element() > maxx:
            maxx = vev.element()
    return maxx

def populate_visited_recursive(visited, vector):
    visited.append(vector)
    for edge in vector.edges:
        for vec in edge.endpoints():
            if vec not in visited:
                populate_visited_recursive(visited, vec)





print('Max fundet med hjemmelavet recursiv metode')
print(str(find_max(v15)))
