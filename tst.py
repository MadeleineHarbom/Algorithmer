
mylist = ['M', 'a', 'd', 'e']

i=0
j=1

print(mylist[i:j])

myrange = range(0, len(mylist))
myrange2 = range(-len(mylist), 0)
print(myrange)
for i in myrange:
    print(i)

for j in myrange:
    print(-j)

print('test')
for i in range(0, len(mylist)):
    templist = []
    for j in range(i, len(mylist)):
        templist.append(mylist[j])
    print(templist)