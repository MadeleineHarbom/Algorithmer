count =0
print(count)

name = 'John Doe'
print(name)


print(type(count))
print(type(name))
print(type(10/3))
print(type(10/3.0))
print(type(10//3))
print(type(10//3.0))


print('E1')
a = 1
print(type(a))
a = 'Hello'
print(type(a))

print('E2')

print(name)
name.lower()
print(name)
print(name.lower())

print('E3')
reserve=name[len(name)::-1]
print(reserve)

print('E4')
first_name = 'Madeleine'
last_name = "Rudkjøbing"
print(first_name + ' ' +last_name)
print((str(len(first_name))))
print(first_name.count('e'))
list1 = [9,8,2,5,2,5,9,7]
print(max(list1))
print(min(list1))

#find hvad in laver
print(first_name[0])
print(first_name[0:4])

print('E5')
listmix = [3, 'Hej', [4,5]]
print(listmix)

print('E6')
dict1 = {"Banana":"Good", "Apple":"Bad", "Peach":"Dangerous"}
for i in dict1:
    print(i + " is " + dict1.get(i))

print('E7')
counter1 = 0
for i in range(1, 100):
    counter1 += i

print(counter1)

counter2 = 0
while counter2 < 100:
    counter2 +=1

print(counter2)

print('E8')

intlist = [1,4,89, 31, 11,78, 56, 82, 1, 8, 4, 9, 38, 30, 29]
for i in intlist:
    if i % 2 == 0:
        print(i)

print('E9')

intlist2 = [1,3,11,33, 7]
intlist3 = []
for i in intlist2:
    if 33%i == 0:
        print(i)
        intlist3.append(i)


print(intlist3)

print('E10')

stringlist= ["to","be","or", "not", "to", "be"]
stringdict = dict()
for i in stringlist:
    stringdict[i] = stringlist.index(i)

print(stringdict)