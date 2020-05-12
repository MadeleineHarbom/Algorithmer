from L11_pattern_matching.text import *

def find_boyer_moore(text, pattern):
    t, p = len(text), len(pattern)
    if p == 0: #hvis pattern er tomt
        return 0
    last = {}
    for k in range(p):
        last[pattern[k]] = k #lavet et array med bogstaverne i pattern som key, og k(int) som value
    i = p-1
    k = p-1
    while i < t:
        print('Checking ' + text[i] + ' at text-index ' + str(i) + 'against ' + pattern[k] + ' at pattern-index ' + str(k))
        if text[i] == pattern[k]: # er det en match
            if k == 0:
                return i
            else:
                i -= 1
                k -= 1 #Her begynder k at ticke ned
        else:
            j = last.get(text[i], -1) #hvad sker her?
            i += p - min(k, j + 1)
            k = p - 1 #sikrer at k er den samme, hvis ikke patern er fundet
    return -1


print(find_boyer_moore(bran, 'morning'))
print(find_boyer_moore(dna, 'CCTTTTGC'))
