# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 21:19:10 2020

@author: jhaj
"""

recusive_counter = 0

def fib_rek(n):
    global recusive_counter
    recusive_counter = recusive_counter + 1
    if n == 1 or n == 2:
        return 1
    return fib_rek(n-1) + fib_rek(n-2)

#print(fib_rek(40))

values = []
def fib_dyn(n):
    global values
    if len(values) == 0:
        values = [0]*(n+1)
        values[1] = 1
        values[2] = 1
    if values[n] != 0:
        return values[n]
    values[n] = fib_dyn(n-1) + fib_dyn(n-2)
    return values[n]
    
     
    
#print(fib_dyn(40))

def cut_rod_rek(prices, n):
    
    if n <= 0:
        return 0
    max_val = prices[n]
    for i in range(1, n):
        max_val = max(max_val, prices[i] + cut_rod_rek(prices, n-i))
    print(f"cut({n})")
    print(max_val)
    return max_val


prices = [0, 1, 5, 8, 9, 10, 17, 17, 20]
print(cut_rod_rek(prices, 7))
print(fib_rek(9))
print(recusive_counter)











