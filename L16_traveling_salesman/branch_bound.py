
from L16_traveling_salesman.adaptable_heap_priority_queue import *
import urllib.request

def pretty_print(sudoku):
    for i in range(9):
        if i % 3 == 0:
            print('')
        s = ''
        for j in range (9):
            if j % 3 == 0:
                s += '   '

            else:
                s += (' ')

            s += str(sudoku[i][j])

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

def create_matrix(matriks):
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
    return total


def set_inf(matriks, row, col):
    matriks[col][row] = float('inf')
    for i in range(len(matriks)):
        matriks[i][col] = float('inf')
        matriks[row][i] = float('inf')
    return matriks


def find_travel(matriks):
    m = create_matrix(matriks)
    r = reduce(m)
    q = AdaptableHeapPriorityQueue() #hvorfor en priority queue?
    q.add(r, (m, 0)) #mængden den blevet recuderet er key, til en tuple med (matrix, level)
    while not q.is_empty():
        key, value = q.remove_min() #går nu den korterste vej
        #remove min returneret (item._key, item._value)
        matrixx, level = value
        for j in range(len(matrixx[level])): #sikker?
            if matriks[level][j] == float('inf'):
                continue #j++
            temp_m = matrixx.copy() #ikke ændre på orginal matrix hvis shit går galt
            set_inf(temp_m, level, j)
            reduction = reduce(temp_m)
            cost = key + matrixx[level][j] + reduction
            q.add(cost, (temp_m, j)) #bygger træet

    return m



imported = import_tsp()
pretty_print(imported)
print('O')
print('  ===============o')
print('O')
tsm_matrix = find_travel(imported)
pretty_print(tsm_matrix)