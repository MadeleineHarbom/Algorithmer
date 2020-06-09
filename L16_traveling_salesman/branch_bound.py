
from L16_traveling_salesman.adaptable_heap_priority_queue import *
from L16_traveling_salesman.travels import *
import urllib.request

def pretty_print(matrixx):
    for i in range(len(matrixx)):

        s = '\n'
        for j in range(len(matrixx[i])):
            s += '   '
            s += str(matrixx[i][j])

        print(s)

def import_tsp():
    dist = []
    for line in urllib.request.urlopen(
        "https://people.sc.fsu.edu/~jburkardt/datasets/tsp/p01_d.txt"):
        l = line.decode('utf-8').strip().split("        ")
        d = []
        for e in l:
            d.append(int(e))
        dist.append(d)
    return dist


def inf_matrix(matriks):
    for i in range(len(matriks)):
        for j in range(len(matriks)):
            if matriks[i][j] == 0:
                matriks[i][j] = float('inf')
    return matriks



def reduce(matriks):
    total = 0
    for i in range(len(matriks)):
        min_row = float('inf')
        for j in range(len(matriks[i])):
            min_row = min(matriks[i][j], min_row)
        if min_row == float('inf'):
            continue # eller kan man ende med at trække infinity fra :P
        for k in range(len(matriks[i])):
            matriks[i][k] -= min_row
        total += min_row

    for i in range(len(matriks)):
        min_col = float('inf')
        for j in range(len(matriks[i])):
            min_col = min(matriks[j][i], min_col)
        if min_col == float('inf'):
            continue #ikke sikker på dette behøves
        for k in range(len(matriks[i])):
            matriks[k][i] -= min_col
        total += min_col
    pretty_print(matriks)
    print('----------------')
    #inf_matrix(matriks)
    pretty_print(matriks)
    print('===================')
    return total


def set_inf_reduce(matriks, row, col):
    matriks[col][row] = float('inf')
    for i in range(len(matriks)):
        #print(matriks[i][col])
        #print(matriks[row][i])
        matriks[i][col] = float('inf')
        matriks[row][i] = float('inf')

    return matriks


def find_travel(matriks):
    m = inf_matrix(matriks)
    r = reduce(m)
    q = AdaptableHeapPriorityQueue() #hvorfor en priority queue?
    q.add(r, (m, 0)) #mængden den blevet recuderet er key, til en tuple med (matrix, level)
    cost = 0
    while not q.is_empty():
        key, value = q.remove_min() #går nu den korterste vej
        #remove min returneret (item._key, item._value)
        matrixx, level = value
        for j in range(len(matrixx[level])): #sikker?
            if matriks[level][j] == float('inf'):
                continue #j++
            temp_m = matrixx.copy() #ikke ændre på orginal matrix hvis shit går galt
            print('Level (uninfed ' + str(level))
            pretty_print(matrixx)
            temp_m = set_inf_reduce(temp_m, level, j)
            print('Level (infed) ' + str(level))
            pretty_print(temp_m)
            reduction = reduce(temp_m)
            cost = key + reduction
            #costie = key + matrixx[level][j] + reduction
            print(cost)
            q.add(cost, (temp_m, j)) #bygger træet
        print(cost)

    return (m, cost)



imported = import_tsp()
pretty_print(dist2)
print('O')
print('  ===============o')
print('O')
tsm_matrix, cost = find_travel(dist2)
pretty_print(tsm_matrix)
print(cost)