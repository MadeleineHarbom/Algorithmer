print('E1')
def e1func(input):
    print(input)

e1func('Hello World')
e1func(4)
e1func([[1,5,8]])

print('E2')
def upto(n):
    ''' adds together all numbers from 1 up to n,
    and returns the value '''
    counter = 0
    for i in range(1, n):
        counter += n

    return counter

print(upto(3))

print('E3')

def addall(alist):
    ''' alist is a list of numbers, and the function
    returns the sum of all the numbers '''
    counter = 0
    for i in alist:
        counter += i

    return counter

print(addall([0,1,2,3]))


def addall_secure(alist):
    ''' alist is a list of numbers, and the function
    returns the sum of all the numbers '''
    counter = 0
    for i in alist:
        if isinstance(i, int):
            counter += i

    return counter

print(addall_secure(["Hej",0,1,2,3]))

print('E4')
def reverse(alist):
    ''' returns the list reversed,
    so e.g [1,2,3] becomes [3,2,1]'''
    newlist = []
    for i in alist:
        newlist.insert(0, i)

    return newlist

print(reverse([0,1,2,3,4,5]))

print('E5')

def minmax(alist):
    ''' alist is a list of integers
    returns a tuple with the minimum
    and the maximum value in the list '''
    mini = min(alist)
    maxi = max(alist)
    return (mini, maxi)

print(minmax([7,1,2,9,4]))

print('E6')

def evennumbers(alist):
    ''' alist is a list of integers
    This function returns a list with
    only the even integers from the list '''
    newlist = []
    for i in alist:
        if i % 2 == 0:
            newlist.append(i)

    return newlist

print(evennumbers([1,2,3,4,5,6,7,8,9]))

print('E7')

def fib(n):
    ''' n=0 or n=1 returns 1
    otherwise return the sum of the
    two previous Fibonacci numbers '''
    if n is 0 or n is 1:
        return 0
    else:
        return n + fib(n-1)


print(fib(2))

print('E8')

obj1 = [1,2,3]
obj2 = obj1
obj2[0] = 5
print(obj1)
print(obj2)

def e8(list):
    list[0] = 99
    print(list)

print(obj1)
e8(obj1)
print(obj1)
print('A functions say more then 1k words')

print('E9')

e9list = [1,2,3,4,5,6,7,8,9]
e9listcopy = e9list.copy()
e9list[0] = 0
e9listcopy[0] = 10
print(e9list)
print(e9listcopy)

print('E10')

def inc_list(alist):
    ''' alist is a list of integers.
    This function will add one to all elements '''
    locallist = alist.copy()
    for i in range(0, len(locallist)):
        locallist[i] = locallist[i]+1

    return locallist

e10list = [1,2,3,4,5]
e10listmodded = inc_list(e10list)
print(e10list)
print(e10listmodded)

print('E11')
dict1 = {'one': 1, 'two':2, 'three':3, 'four':4, 'five':5}
dict2 = dict1
dict2['one'] = 5
print(dict1)
print(dict2)

def inc_dict(adict):
    localdict = adict.copy()
    for i in localdict:
        print(adict.get(i))
        localdict[i] = localdict.get(i) + 1

    return localdict

dict3 = {'one': 1, 'two':2, 'three':3, 'four':4, 'five':5}
print(inc_dict(dict3))
print(dict3)

print('E12')
def countwords(alist):
    ''' alist is a list of strings
    returns a dictionary, with a count of each string.'''
    localdict = dict()
    for i in alist:
        if i in localdict:
            localdict[i] = localdict.get(i) +1
        else:
            localdict[i] = 1

    return localdict

wordlist= ['hej', 'diller', 'noidea', 'word', 'poopie', 'hej', 'word']
print(countwords(wordlist))