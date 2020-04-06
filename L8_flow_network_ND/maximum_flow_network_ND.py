import math

from L8_flow_network_ND.Flow_directed_adjacency_list_graph import *

def ford_fulkerson(graph : FlowGraph, start : DiectedVertex, sink: DiectedVertex):
    mini = math.inf
    maxx = 0
    triversed = [start] #for at tjekke for cirkler
    for edge in start.edges():
        ford_fulkerson_rekursive(graph, start, sink, edge, triversed, mini, maxx)
        #ændre på alt



def ford_fulkerson_rekursive(graph, start, sink, current_edge, trivered, minn, maxx):
    endpoint = current_edge.endpoint()
    if endpoint == start or endpoint in trivered:
        print('back at start, abort abort abort')
        return
    else:
        if current_edge.unused_capacity() > maxx:
            maxx = current_edge.unused_capacity()
        if current_edge.unused_capacity() < minn:
            minn = current_edge.unused_capacity()
    if endpoint == sink:
        print('Yay, goooaaaal, go back :D')
        #update
        return maxx
    else:
        trivered.append(endpoint)
        for edge in endpoint.edges():
            ford_fulkerson_rekursive(graph,start, sink, edge, trivered, minn, maxx)




