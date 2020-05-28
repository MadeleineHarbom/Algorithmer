from Obligatorisk_Opgave_2.a_2014_graph import *

#TODO kan jeg ikke skrive dette pænere

#n er en integer. Antallet lufthavner
#m er en integer. Antaller routes
#routes er en list of Routes
#Routes er 3 integers. Lufthavn A, Lufthavn B, antal lounges

def A_2014(n, m, routes):
    graph = Graph()
    for airport in range(1, n+1):
        #alle airports kommer til at ligge i grafen og kan trækkes ud når man laver edges
        graph.insert_vertex(airport)



    for route in routes:
        #[start, stop, lounges]
        v1 = graph.find_vertex(route[0])
        v2 = graph.find_vertex(route[1])
        graph.insert_edge(route[2], v1, v2)

   # print_graph(graph)


    all_edges = graph.edges()
    total_number_lounge = None
    for edge in all_edges:
        for v in edge.endpoints():
            triversed = []
            result = None
            result = rec_check(graph=graph, edge=edge, vertex=v, trivesed=triversed)
            if result > 0:
                total_number_lounge = result
    return total_number_lounge









def rec_check(graph, edge, vertex, trivesed):
    if edge in trivesed:
        if edge.element() == edge.number_of_lounges():
            return 0
        else:
            return -400000
    trivesed.append(edge)
    if edge.element() == 0:
        for v in edge.endpoints():
            if v.has_lounge():
                return -400000
    elif edge.element() == 2:
        added = vertex.give_lounge()
        added += graph.opposite(vertex, edge).give_lounge()
        for v in edge.endpoints():
            #added = v.give_lounge()
            oposite = graph.opposite(v, edge)
            for edgie in oposite.edges():
                if edge != edgie:
                    return rec_check(graph=graph, edge=edgie, vertex=graph.opposite(v, edge), trivesed=trivesed) + added
    else: #1
        #endpoints = edge.endpoints()
        if edge.endpoints()[0].has_lounge() and edge.endpoints()[1].has_lounge():
            return -400000
        elif vertex.has_lounge():
            opo = graph.opposite(vertex, edge)
            #added = opo.give_lounge()
            for edgeieie in opo.edges():
                if edgeieie != edge:
                    return rec_check(graph=graph, edge=edgeieie, vertex=opo, trivesed=trivesed) + 0
        else:
            opo = graph.opposite(vertex, edge)
            added = opo.give_lounge()
            for edginator in opo.edges():
                if edginator != edge:
                    return rec_check(graph=graph, edge=edginator, vertex=opo, trivesed=trivesed) + added
    return -300




def print_graph(graph):
    v_iter = graph.vertices()
    print('Verticies')
    for x in v_iter:
        print(x.element())

    e_iter = graph.edges()
    print('Edges')
    for y in e_iter:
        print(y.element())



