from L6_propritering_heaps_ND.TheObject import AnObject

#implement your own priority queue, using a heap

#træet bliver lavet som array

class ArrayHeap():
    def __init__(self):
        self.theQ = []

    def add(self, objectt):
        #TODO fix så keys ikke skal være unikke
        if len(self.theQ) == 0:
            self.theQ.append(objectt)
            return
        elif len(self.theQ) == 1:
            if objectt.key < self.theQ[0].key:
                self.theQ.insert(0, objectt)
                return
            else:
                self.theQ.append(objectt)
                return

        for i in range(0, len(self.theQ)-1):
            if objectt.key > self.theQ[i].key and objectt.key < self.theQ[i+1].key:
                self.theQ.insert(i, objectt)
                return
        self.theQ.append(objectt)


for i in range(0, 10):
    print(i)


print('----------------')

leQ = ArrayHeap()

leQ.add(AnObject(7, '7'))

leQ.add(AnObject(9, '9'))

leQ.add(AnObject(1, '1'))

leQ.add(AnObject(12, '12'))

leQ.add(AnObject(6, '6'))

leQ.add(AnObject(2, '2'))

leQ.add(AnObject(8, '8'))

leQ.add(AnObject(3, '3'))

for item in leQ.theQ:
    print(item.value)



