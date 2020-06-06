#At ha træet i en liste gør det nemmere at finde "børnene", gennem at tage n*2+what? (position*2+1 og position*2+2)
from L6_propritering_heaps_ND.TheObject import AnObject

class Heap:

    def __init__(self):
        self._queue = []

    def __len__(self):
        return len(self._queue)

    def _parent(self, position):
        return (position-1) // 2

    def _left(self, position):
        return 2*position + 1

    def _right(self, position):
        return 2*position + 2

    def _has_right(self, position):
        return self._right(position) < len(self._queue)

    def _has_left(self, position):
        return self._left(position) <len(self._queue)

    def _swap(self, i, j):
        self._queue[i], self._queue[j] = self._queue[j], self._queue[i]

    def _upheap(self, position):
        parent = self._parent(position)
        if position > 0 and self._queue[position].obj < self._queue[parent].obj:
            self._swap(position, parent)
            self._upheap(parent)

    def _downheap(self, position):
        if self._has_left(position):
            left = self._left(position)
            small_child = left  # although right may be smaller
            if self._has_right(position):
                right = self._right(position)
                if self._queue[right] < self._queue[left]:
                    small_child = right
                if self._queue[small_child] < self._queue[position]:
                    self._swap(position, small_child)
                    self._downheap(small_child)  # recur at position of small child

    def insert(self, proirity, content):
      
        self._queue.append(HeapContainer(proirity, content))
        self._upheap(len(self)-1)

    def min(self):
        if self.is_empty():
            raise Exception('Priority queue is empty.')
        item = self._queue[0]
        return (item._key, item._value)

    def remove_min(self):
        if self.is_empty():
            raise Exception('Priority queue is empty.')
        self._swap(0, len(self._queue) - 1)  # put minimum item at the end
        item = self._queue.pop()    # and remove it from the list;
        self._downheap(0)                            # then fix new root
        return (item._key, item._value)

    def is_empty(self):
        return len(self) == 0







class HeapContainer:

    def __init__(self, prio, obj):
        self.prority = prio
        self.obj = obj
