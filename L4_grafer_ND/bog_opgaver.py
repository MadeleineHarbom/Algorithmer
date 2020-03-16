from L4_grafer_ND.adjacency_list_graph import *

def create_matrix(m, n):
    return [[0 for y in range(m)] for x in range(n)]

def print_matrix(matrixx):
    for i in range(0, len(matrixx)):
        print(matrixx[i])

#14_3 draw and adjecency matrix represention of the udirected graf shown in figure 14.1
print('14_3')
nodes = [
Vertex('Snoeyink'), #0
Vertex('Goodrich'), #1
Vertex('Garg'), #2
Vertex('Goldwasser'), #3
Vertex('Tollis'), #4
Vertex('Vitter'), #5
Vertex('Tarmassia'), #6
Vertex('Preparata'), #7
Vertex('Chiang')] #8

edgematrix = create_matrix(len(nodes), len(nodes))

#snoeyink - goodrich
edgematrix[0][1] = 1
edgematrix[1][0] = 1

#goodrich - garg
edgematrix[1][2] = 1
edgematrix[2][1] = 1

#goodrich - goldwasser
edgematrix[1][3] = 1
edgematrix[3][1] = 1

#goodrich - tollis
edgematrix[1][4] = 1
edgematrix[4][1] = 1

#goodrich - vitter
edgematrix[1][5] = 1
edgematrix[5][1] = 1

#goodrich - tarmassia
edgematrix[1][6] = 1
edgematrix[6][1] = 1

#garg - tarmassia
edgematrix[3][6] = 1
edgematrix[6][3] = 1

#goldwasser - tarmassia
edgematrix[3][6] = 1
edgematrix[6][3] = 1

#tollis - tarmassia
edgematrix[4][6] = 1
edgematrix[6][4] = 1

#tollis - vitter
edgematrix[4][5] = 1
edgematrix[5][4] = 1

#vitter - tarmassia
edgematrix[6][5] = 1
edgematrix[5][6] = 1

#vitter - preparata
edgematrix[7][5] = 1
edgematrix[5][7] = 1

#tarmassia - preparata
edgematrix[6][7] = 1
edgematrix[7][6] = 1

#chiang -  tarmassia
edgematrix[8][6] = 1
edgematrix[6][8] = 1

#chiang - prepatara
edgematrix[7][8] = 1
edgematrix[8][7] = 1

#chiang - goodrich
edgematrix[1][8] = 1
edgematrix[8][1] = 1

print_matrix(edgematrix)

#14_4 draw and adjecency list represention of the udirected graf shown in figure 14.1
print('14_4')
snoeyink = Vertex('Snoeyink'),
goodrich = Vertex('Goodrich'),
garg = Vertex('Garg'),
goldwassser = Vertex('Goldwasser'),
tollis = Vertex('Tollis'),
vitter = Vertex('Vitter'),
tarmassia = Vertex('Tarmassia'),
preparata = Vertex('Preparata'),
chiang = Vertex('Chiang')
edgelist = {
    (snoeyin, {}),
    (goodrich, {}),
    (garg, {})
}


#14_6 Suppose we represent a graph G having n vertices and m edges with the eddge list structure.
# Why, in this case, does the insert_edge(u,v,x) in O(1) time while the remove_vertex method runs in O(m) time?

#14_7 Gave psudo code for performing an insert_edge (u,v,x) using the adjecency matrix representation





