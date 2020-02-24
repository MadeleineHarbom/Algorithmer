#Lave fibbenuchi iterativt

counter = 0



def fib_iterative(n):
    global counter

    i = 2
    thelist = []
    thelist.append(1)
    thelist.append(1)
    while i <= n:
        counter = counter + 1
        thelist.append(thelist[i-1] + thelist[i-2])
        i = i+1

    return thelist


print(fib_iterative(40))
print(counter)