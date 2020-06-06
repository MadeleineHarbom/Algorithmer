#Lave fibbenuchi iterativt


#antagelse fib(0)=0 og fib(1)=1

print()
print()
print()

recursive_counter = 0
dynamic_counter = 0

def fib_dynamic(n):
    global dynamic_counter
    if n == 0:
        return 0
    elif n == 1:
        return 1
    i = 2
    fib = [0,  1]
    while i <= n:
        dynamic_counter = dynamic_counter + 1
        fib.append(fib[i-2] + fib[i-1])
        i += 1
    return fib[n]


def fib_recursive(n):
    global recursive_counter
    recursive_counter = recursive_counter +1
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib_recursive(n-2) + fib_recursive(n-1)



fib_dynamic(20)
fib_recursive(20)
print('For finding the 20th fibonacci number')
print('The dynamic fibonacci while-loop ran ' + str(dynamic_counter) + ' times.')
print('The recurive fibobonacci function ran ' + str(recursive_counter) + ' times.')