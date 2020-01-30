import functools

print('E1')

def add1(number):
    return number+1

def sub1(number):
    return number-1

def apply_all(number, alist):

    for func in alist:
        number = func(number)
    return number

print(apply_all(1, [add1, add1, add1]))

print('E2')

def mymap(alist, func):
    locallist = []
    for i in alist:
        locallist.append(func(i))

    return locallist

print(mymap([1,2,3,4,5,6], add1))

print('E3')

def even(x):
    return x % 2 == 0

def myfilter(func, alist):
    locallist = []
    for i in alist:
        if (func(i)):
            locallist.append(i)

    return locallist

print(myfilter(even, [1,2,3,4,5,6]))

print('E4')
def funny(p):
    return p(1)

list4 = list(map(funny,[add1,sub1,even]))
print(list4)

print('den kører functionen funny på hver objet i listen')
print('i dette tilfælde er listen fyldt med funktioner')
print('funnt tager altså hver af disse tre fuktioner og kører dem med 1 som argument')
print('Adderer 1 til 1 (2), fjerer 1 fra 1 (0), tjekker hvis en er lige (false)')

print('E5')
def add(x, y):
    return x+y

print(functools.reduce(add, range(1,10)))
print(functools.reduce(add, range(1,100)))

print('E6')

def twice(func):
    def innerfunc(number):
        inner = func(number)

        return func(inner)
    return innerfunc

f = twice(add1)
number = f(3)
print(number)

print('E7')
e7list = apply_all(1, [lambda x: 1+x, lambda x: 1+x, lambda x: 1+x])
print(e7list)
filtered = list(map(add1, [1, 2, 3, 4, 5, 6]))

print(filtered)


