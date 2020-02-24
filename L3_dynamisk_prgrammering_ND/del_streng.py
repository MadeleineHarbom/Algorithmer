

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
        print("index: ")
        print("i: " + str(i))
        if i < len(thearray1):
            for j in range(i, len(thearray1)):
                print("j: " + str(j))
                print(thearray1[i:j + 1])
                for k in range(0, len(thearray2)):
                    print(k) #TODO





print_alle_delstrenge("Made")