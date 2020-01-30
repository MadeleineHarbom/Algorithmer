class Dog:

    def __init__(self, name):
        self._name = name

    def name(self):
        return self._name


class Person:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def name(self):
        return self.first + " " + self.last

