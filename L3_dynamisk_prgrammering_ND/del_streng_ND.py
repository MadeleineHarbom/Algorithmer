

def print_alle_delstrenge(thestring):
    #thedict = thestring.toCharArray()
    thearray = list(thestring)
    print(thearray)
    for i in range(0, len(thearray)):
        print("index: ")
        print("i: " + str(i))
        if i < len(thearray):
            for j in range(i, len(thearray)):
                print("j: " + str(j))
                print(thearray[i:j+1])


def find_laengste_delstreng(string1, string2):
    thearray1 = list(string1)
    thearray2 = list(string2)
    longeststring = ''
    print(thearray1)
    print(thearray2)
    for i in range(0, len(thearray1)):
        if j < len(thearray2):
            if i == j:
                tempstring = ''
                print('Match')
                add = 0
                while thearray1[i+add] == thearray2[j+add]:
                    tempstring.append(thearray1[i+add])
                if len(tempstring) > len(longeststring):
                    longeststring = tempstring
    return longeststring






find_laengste_delstreng('Made', 'Madeleine')