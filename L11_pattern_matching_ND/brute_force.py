
def find_brute(text, pattern):
    t, p = len(text), len(pattern)
    for i in range(t-p + 1):
    #da man ikke behøver gå længere ind i texten, når det ikke er plads nok tilbage til at passe pattern
        p_index = 0
        while p_index < p and text[i + p_index] == pattern[p_index]:
            #while pindex er under pattern length og der er en match
            p_index += 1
        if p_index == p:
            #hele pattern er fundet
            return i
        return -1

