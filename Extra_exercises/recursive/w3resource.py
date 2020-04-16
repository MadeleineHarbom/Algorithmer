
print('1. Write a Python program to calculate the sum of a list of numbers')

def sum(thearray):
    if len(thearray) == 1:
        return thearray[0]
    else:
        num = thearray[0]
        thearray.pop(0)
        return num + sum(thearray)


anarray = [1, 2, 3, 4, 5]

print(sum(anarray))

print('3. Write a Python program of recursion list sum.')

#data list kan indholde ints, eller lister med ints
def list_sum(data_list):
    total = 0
    for element in data_list:
        if type(element) == type([]):
            total = total + list_sum(element) #hvis elementet er en liste, kalder metoden sig selv på den
        else:
            total = total + element
    return total

print(list_sum([1, 2, [3,4],[5,6]]))

print('4. Write a Python program to get the factorial of a non-negative integer')
def fractoral(number):
   if number <= 1:
        return 1
   else:
       return number * fractoral(number-1)


print(fractoral(5))

print('5. Write a Python program to solve the Fibonacci sequence using recursion')

def fibonacci(i):
    if i <= 2: #du skal kunne addere de de to tal før
        return 1
    else:
        return fibonacci(i - 1) + fibonacci(i - 2)


print(fibonacci(6))

print('6. Write a Python program to get the sum of a non-negative integer')

def sum_digits(i: int):
    if i == 0:
        return 0
    else:
        return i % 10 + sum_digits(int(i / 10))
        #%10 giver den entallet, og int(i/10) fjerner det, så bliver 10-tallet det nye ental

print(sum_digits(1234))

print('7. Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0)')

def sum_series(i):
    if i > 2:
        return i + sum_series(i-2)
    else:
        return i

print(sum_series(6))
print(sum_series(10))

print('8. Write a Python program to calculate the harmonic sum of n-1 '
      '(The harmonic sum is the sum of reciprocals of the positive integers)')

def harmonic_sum(n):
    if n == 1:
        return 1
    else:
        return 1/n + harmonic_sum(n-1)

print(harmonic_sum(3))

print('10. Write a Python program to calculate the value of a to the power of b')

def power(a, b):
    if b == 1:
        return a
    else:
        return a * power(a, b-1)

print(power(2, 4))

