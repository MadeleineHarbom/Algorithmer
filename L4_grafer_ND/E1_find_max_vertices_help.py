from L4_grafer_ND.eksempel.edge_list_graph import *

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


def find_max_travilal(graf):
    v_iter = graf.vertices()

    v_max = -9000

    for x in v_iter:
        if x.element() > v_max:
            v_max = x.element()

    return v_max

#TODO spørg lærer
#Efter at ha afholdt en lille think-tank for meget kloge mennesker <host host>
#I spørgsmålet hvor du skal fidne alle noget i en edge list graf med en metode der tager grafen og ev en vertex som input
#At finde alle knude udefra en anden knude giver for mig ikke mening i en edge list graf, da alt går ud fra edge
#og knuderne ikke indholder andet end objektet de skal "bære"


#slet derfra og ned
def find_max(adjacency_graph, first):
    visited = []
    visited.append(first)

    for edge in first.edges:
        for endpoint in edge.endpoints():
            find_max_helper(visited, endpoint)
    maxi = visited[0]
    for element in visited:
        if element.element() > maxi.element():
            maxi = element

    return maxi

def find_max_helper(visited, node):
    edges = node.enpoints()
    for edge in edges:
        for endpoint in edge.endpoints():
            if endpoint not in visited:
                visited.append(endpoint)
                return find_max_helper(visited, endpoint)
    return None


print(find_max(graph, v15))