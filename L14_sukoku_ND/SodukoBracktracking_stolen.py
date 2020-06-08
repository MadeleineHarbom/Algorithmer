# -*- coding: utf-8 -*-+
"""
Created on Fri Apr 17 10:31:24 2020

@author: lokel
"""

a = [
    [5,3,0, 0,7,0, 0,0,0],
    [6,0,0, 1,9,5, 0,0,0],
    [0,9,8, 0,0,0, 0,6,0],
    
    [8,0,0, 0,6,0, 0,0,3],
    [4,0,0, 8,0,3, 0,0,1],
    [7,0,0, 0,2,0, 0,0,6],
    
    [0,6,0, 0,0,0, 2,8,0],
    [0,0,0, 4,1,9, 0,0,5],
    [0,0,0, 0,8,0, 0,7,9]
]

#Tjekker en række for om et givet tal er i den.
def checkRow(arr, row, value):
    for i in arr[row]:
        if i == value:
            return True
    return False

print("Expected to be True: " + str(checkRow(a, 1, 5)))
print("Expected to be False: " + str(checkRow(a, 0, 8)))

# Tjekker en colonne for om et givet tal er i den.
def checkColumn(arr, col, value):
    for e in arr:
        if e[col] == value:
            return True
    return False

print("Expected to be True: " + str(checkColumn(a, 0, 5)))
print("Expected to be False: " + str(checkColumn(a, 2, 3)))


# Tjeker om et tal er i en firkant
def checkSqare(arr, row, col, value):
    cornerRow = row - row%3
    cornerCol = col - col%3
    rows = 0
    for i in range(cornerRow, cornerRow + 3):
        if arr[i][cornerCol] == value or  arr[i][cornerCol + 1] == value or  arr[i][cornerCol + 2] == value:
            return True
        rows += 1
    return False

print("Expected to be True: " + str(checkSqare(a, 2, 2, 5)))
print("Expected to be False: " + str(checkSqare(a, 2, 5, 6)))


#Finder en tom plads og retunere koordinaterne
def find_empty(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 0:
                return (i, j)
    return None

# Finder en tom plads og prøver alle tal som kan passe på den plads rekursivt
def try_it(arr):
    find = find_empty(arr)
    if not find:
        print_pretty(arr)
        return True
    for i in range(1, 10):
        if checkRow(arr, find[0], i) == False and checkColumn(arr, find[1], i) == False and checkSqare(arr, find[0], find[1], i) == False:
            arr[find[0]][find[1]] = i
            try_it(arr)
            arr[find[0]][find[1]] = 0
    return False
    
# Printer det pænt ud
def print_pretty(arr):
    row = 1
    for e in arr:
        count = 1
        word = ""
        for i in e:
            word += str(i) + " "
            if count%3 == 0:
                word += "   "
            count += 1
        print(word)
        if row%3 == 0:
            print()
        row += 1

print_pretty(a)

print("---------------------------------------------")
   
try_it(a) 
       
