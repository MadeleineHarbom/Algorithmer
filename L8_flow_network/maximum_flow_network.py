import math

from L8_flow_network.Flow_directed_adjacency_list_graph import *

def ford_fulkerson(graph : FlowGraph, start : DiectedVertex, sink: DiectedVertex):

    #triversed = [start] #for at tjekke for cirkler
    #edges = []
    #triversed kunne tænkes være smart at ha som en stack, da i augmented flow ville en stafck passe perfekt
    #dog skal triversed også kunne tjekker for cirkler, hvilket ikke kan gøres uder bølv i en stack
    results = [9]
    while len(results) > 0:

        results =[]
        for edge in start.edges():
            triversed = [start]
            edges = []
            mini = 900
            mini = ford_fulkerson_rekursive(graph, start, sink, edge, triversed, 9000, edges)
            edge.add_flow(mini)
            if mini != 0:
                results.append(mini)




#tjekker ikke for negative
def ford_fulkerson_rekursive(graph, start, sink, current_edge, trivered, minn, edges):
    print(minn)
    endpoint = current_edge.endpoint()
    if endpoint in trivered:
        print('back at start, abort abort abort')
        return 0
    else:
        edges.append(current_edge)
        if current_edge.unused_capacity() < minn:
            minn = current_edge.unused_capacity()
    if endpoint == sink:
        print('Yay, goooaaaal, go back :D')
        return minn
    else:
        trivered.append(endpoint)
        for edge in endpoint.edges():
            edges.append(edge)
            value = ford_fulkerson_rekursive(graph, start, sink, edge, trivered, minn, edges)
            print('element' + edge.element() + ':  ' + str(value))
            if value != 0:
                if value < minn:
                    minn = value
            edge.add_flow(value)
        return value


            #her skal maxx og min tjekkes




