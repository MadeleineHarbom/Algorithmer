

def print_alle_delstrenge(thestring):
    mylist = list(thestring)
    for i in range(0, len(mylist)):
        templist = []
        for j in range(i, len(mylist)):
            templist.append(mylist[j])
        print(templist)



def find_laengeste_delstreng_opgave2_for_loops(string1, string2):
    thearray1 = list(string1)
    thearray2 = list(string2)
    longeststring = ''
    for i in range(0, len(string1)):
        for j in range(0, len(string2)):
            if string1[i] == string2[j]:
                print('match: ' + string1[i] + ' og ' + string2[j])
                delstring = ''
                add = 0
                while i+add < len(string1) and j+add < len(string2):
                    if string1[i+add] == string2[j+add]:
                        delstring += string1[i+add]
                        add += 1
                    else:
                        print('immaouto break')

                        break
                if len(delstring) > len(longeststring):
                    longeststring = delstring
    return longeststring

def find_laengste_delstreng_opgave3_matrix(string1, string2):
    matrixx = create_matrix(len(string1) + 1, len(string2) + 1)
    for i in range(1, len(string1)):
        for j in range(1, len(string2)):
            if string1[i] == string2[j]:
                matrixx[i][j] = matrixx[i-1][j-1] + 1
    print_matrix(matrixx)

def create_matrix(m, n):
    return [[0 for y in range(m)] for x in range(n)]


def print_matrix(matrixx):
    for i in range(0, len(matrixx)):
        print(matrixx[i])





#print_alle_delstrenge('Made')
#print(find_laengeste_delstreng_opgave2('Made', 'Make'))
print(find_laengeste_delstreng_opgave2_for_loops('piskeris', 'malerisk'))
print('Tidskomplesiteten for find længste delstren er...') #TODO
find_laengste_delstreng_opgave3_matrix('piskeris', 'malerisk')

#TODO få den længste delstreng fra matrix læøsningen
#TODO Hvad er tidskompleksiteten på matrix?
#TODO Hvorfor er dette dynamisk programmering