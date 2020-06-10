#TODO
prices = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

recursive_counter = 0
dynamic_counter = 0

#n er længden af staven, giggedy
def cut_rod_rek(prices, n):
    recursive_counter = 0
    recursive_counter += 1
    if n <= 0:
        return 0
    max_val = prices[n]
    for i in range(1, n):
        max_val = max(max_val, prices[i] + cut_rod_rek(prices, n-i))
    return max_val

def cut_rod_dyn(prices, n):
    global dynamic_counter
    values = [0 for x in range(n+1)]
    #if n == 0:
     #   return 0
    for i in range(1, n+1): #måske +1
        maxx = 0
        for j in range(i):
            maxx = max(maxx, prices[j] + values[i -j -1]) #Hvad laver     values[i -j -1]
        values[i] = maxx
    return values[n]



cut_rod_rek(prices, 7)
print(str(cut_rod_rek(prices, 7)))
print(str(cut_rod_dyn(prices, 7)))

