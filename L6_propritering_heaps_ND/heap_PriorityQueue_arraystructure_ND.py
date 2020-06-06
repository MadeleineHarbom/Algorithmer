#At ha træet i en liste gør det nemmere at finde "børnene", gennem at tage n*2+what? (position*2+1 og position*2+2)

class Heap:

    def __init__(self):
        self._queue = []

    def _parent(self, position):
        return (j-1) // 2

    def _left(self, position):
        return 2*position +1

    def _right(self, position):
        return 2*position +2

    def _has_right(self, position):
        return self._right(position) < len(self._queue)

    def _has_left(self, position):
        return self._left(position) <len(self._queue)

    def _swap(self, i, j):
        self._queue[i], self._queue[j] = self._queue[j], self._queue[i]

    def add(self, proirity, containt):
        self._queue.append(HeapContainer(proirity, containt))

    def _upheap(self, position):
        parent = self._parent(position)
        if j > 0 and self._queue[position] < self._queue[parent]:
            self._swap(position, parent)
            self._upheap(parent)

    def _downheap(self, position):
        if self._has_left(position):
            left = self._left(position)
            #TODO fortsæt her




class HeapContainer:

    def __init__(self, prio, obj):
        self.prority = prio
        self.obj = obj
