#Opgave E: 25%
#n er en integer. Antal huse
#h er en list af integers. Deres højde
def E_2014(n, h):
    if n > 0:
        maxx = max(h)
        if maxx > n or maxx == n:
            h.remove(maxx)
            n -= 1
            return E_2014(n, h) +1
        else:
            for house in range(len(h)-1, -1, -1): #TODO make prettier
                if h[house] == 1:
                    h.remove(h[house]) #remove from index instead
                    n -= 1
                else:
                    h[house] -= 1
        return E_2014(n, h) + 1
    else:
        return 0


print(E_2014(6, [2, 1, 8, 8, 2, 3]))
