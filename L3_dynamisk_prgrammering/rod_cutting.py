#TODO
prices = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]



#n er længden af staven, giggedy
def cut_rod_rek(prices, n):
    if n <= 0:
        return 0
    max_val = prices[n]
    for i in range(1, n):
        max_val = max(max_val, prices[i] + cut_rod_rek(prices, n-i))
    return max_val

cut_rod_rek(prices, 7)
print(str(cut_rod_rek(prices, 7)))

