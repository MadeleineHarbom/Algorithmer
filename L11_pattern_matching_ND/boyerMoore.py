from L11_pattern_matching_ND.text import *

def find_boyer_moore(text, pattern):
    t, p = len(text), len(pattern)
    if p == 0: #hvis pattern er tomt
        return 0
    last = {}
    for p_index in range(p): #nok forkert
        last[pattern[p_index]] = p_index #lavet et dictionary med bogstaverne i pattern som key, og pindex(int) som value
    i = p-1
    p_index = p-1
    while i < t:
        #print('Checking ' + text[i] + ' at text-index ' + str(i) + 'against ' + pattern[pindex] + ' at pattern-index ' + str(pindex))
        if text[i] == pattern[p_index]: # er det en match
            if p_index == 0:
                #Hvis p_index er nul, har hele pattern blevet tjekket og matchet, det det begynder bagfra
                return i
            else:
                i -= 1
                p_index -= 1 #Her begynder pindex at ticke ned
        else:
            j = last.get(text[i], -1) #-1 en er default. Hvis key ikke findes, retuneres default
            i += p - min(p_index, j + 1)
            p_index = p - 1  #sikrer at pindex er den samme, hvis ikke patern er fundet
    return -1


print(find_boyer_moore(bran, 'morning'))
print(find_boyer_moore(dna, dnapattern))
