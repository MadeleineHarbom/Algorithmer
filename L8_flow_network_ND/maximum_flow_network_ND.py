import math

from L8_flow_network_ND.Flow_directed_adjacency_list_graph import *

def ford_fulkerson(graph : FlowGraph, start : DiectedVertex, sink: DiectedVertex):
    mini = 9000 #skal være Math.inf
    print(mini)
    #maxx = 0
    triversed = [start] #for at tjekke for cirkler
    edges = []
    #triversed kunne tænkes være smart at ha som en stack, da i augmented flow ville en stafck passe perfekt
    #dog skal triversed også kunne tjekker for cirkler, hvilket ikke kan gøres uder bølv i en stack
    for edge in start.edges():
        ford_fulkerson_rekursive(graph, start, sink, edge, triversed, mini, edges)
        #ændre på alt'



#tjekker ikke for negative
def ford_fulkerson_rekursive(graph, start, sink, current_edge, trivered, minn, edges):
    print(minn)
    endpoint = current_edge.endpoint()
    if endpoint in trivered:
        print('back at start, abort abort abort')
        return 0
    else:
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
            if value != 0:
                edge.add_flow(value)
                return value


            #her skal maxx og min tjekkes




