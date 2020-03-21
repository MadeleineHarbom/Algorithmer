#think I might have misunderstood when I wrote this
#a heap isnt a tree? Should it be an array?
class Heap:

    def __init__(self):
        self.root = None
        print('init')

    def insert(self, objectt):
        if self.root is None:
            self.root = objectt
            print('setting new root <glee>')
        else:
            if self.root.left is None:
                self.root.left = objectt
            elif self.root.right is None:
                self.root.right = objectt

    def recursiveinsert(self, parent, current, objectt):
        if objectt.key == current.key:
            #listen kræver pt unikke keys
            print('phail')
            return
        elif objectt.key > current.key:
            if current.right is not None:
                print('going left :(')
                self.recursiveinsert(current.right, objectt)
            else:
                current.right = objectt
                print('inserted:' + objectt.value + ' to the right of ' + current.value)
                return
        else:
            if current.left is not None:
                print('Going left :D')
                self.recursiveinsert(current.left, objectt)
            else:
                current.right = objectt
                print('inserted:' + objectt.value + ' to the left of ' + current.value)
                return
